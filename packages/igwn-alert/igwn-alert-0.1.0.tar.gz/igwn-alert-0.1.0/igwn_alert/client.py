# Copyright (C) Alexander Pace (2021)
# Copyright (C) Duncan Meacher (2021)
#
# This file is part of igwn_alert
#
# igwn_alert is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# It is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with igwn_alert.  If not, see <http://www.gnu.org/licenses/>.

import logging
from safe_netrc import netrc
from urllib.parse import urlparse, ParseResult
from datetime import timedelta
import json
from json import JSONDecodeError

from hop import Stream
from hop import auth as hop_auth
from hop.auth import Auth
from hop.list_topics import list_topics

import warnings

__all__ = ('client', 'DEFAULT_SERVER',
           'DEFAULT_PORT', 'DEFAULT_GROUP')

log = logging.getLogger(__name__)

DEFAULT_SERVER = 'kafka://kafka.scimma.org/'
DEFAULT_PORT = 9092
DEFAULT_GROUP = 'gracedb'
DEFAULT_BATCH_SIZE = 1
DEFAULT_BATCH_TIMEOUT = timedelta(seconds=0.05)


class client(Stream):
    """A hop-scotch client configured for LVAlert

    Parameters
    ----------
    username : str (optional)
        The SCIMMA username, or :obj:`None` to look up with hop auth or netrc.
    password : str (optional)
        The SCIMMA password, or :obj:`None` to look up with hop auth or netrc
    auth : :class:`Auth <hop.auth.Auth>` (optional)
        A :code:`hop.auth.Auth` object.
    authfile : str (optional)
        Path to hop :code:`auth.toml`
    noauth : bool (optional)
        Set to `True` for unauthenticated session
    group : str (optional)
        GraceDB group (e.g., `gracedb`, `gracedb-playground`)
    server : str (optional)
        The server host (i.e., kafka://.....)
    port : int (optional)
        The server port

    Example
    -------

    Here is an example for listing topics:

    .. code-block:: python

        alert_client = client(group='lvalert-dev')
        topics = alter_client.get_topics()

    Here is an example for running a listener.

    .. code-block:: python

        def process_alert(topic, payload):
            if topic == 'cbc_gstlal':
                alert = json.loads(payload)
                ...

        client = IGWNAlertClient(group='lvalert-dev')
        topics = ['superevent', 'cbc_gstlal']
        client.listen(process_alert, topics)

    """

    def __init__(self, username=None, password=None, auth=None, authfile=None,
                 noauth=False, group=None, server=None, port=None,
                 batch_size=None, batch_timeout=None):

        # Set up variables:
        if server:
            self.server = server
        else:
            self.server = DEFAULT_SERVER

        if port:
            self.port = port
        else:
            self.port = DEFAULT_PORT

        if group:
            self.group_prefix = group
        else:
            self.group_prefix = DEFAULT_GROUP

        if batch_size:
            self.batch_size = batch_size
        else:
            self.batch_size = DEFAULT_BATCH_SIZE

        if batch_timeout:
            self.batch_timeout = batch_timeout
        else:
            self.batch_timeout = DEFAULT_BATCH_TIMEOUT

        # Construct the base url prefix for this session.

        self.base_url_prefix = self._construct_base_url()

        # Initiate the session dict:
        self.sessions = {}

        # Construct hop.auth.Auth object.
        # The order it checks is:
        #   1) Username AND password
        #   2) User-desribed location of toml auth file.
        #   3) Default location of toml auth file ($HOME/.config/hop/auth.toml)
        #   4) .netrc file ($HOME/.netrc)

        if noauth:
            auth = False
        else:
            if (username and password):
                auth = Auth(username, password)
            elif bool(username) != bool(password):
                raise RuntimeError('You must provide both a username and a '
                                   'password for basic authentication.')
            elif authfile:
                auth = hop_auth.load_auth(authfile)
            else:
                try:
                    auth = hop_auth.load_auth()
                except Exception:
                    try:
                        netrc_auth = netrc().authenticators(self.server)
                    except IOError:
                        raise Warning("No authentication found. Proceeding "
                                      "with unathenticated session")
                        auth = False
                    else:
                        if netrc_auth is not None:
                            auth = Auth(netrc_auth[0], netrc_auth[2])

        # Retain the hop.auth.Auth obj
        self.auth_obj = auth

        super().__init__(auth=auth)

    def _construct_base_url(self):
        """
        Contruct the URL, port, and group path for this session
        """

        # parse server URL:
        old = urlparse(self.server)

        # construct full URL, with group prefix:
        return ParseResult(scheme=old.scheme,
                           netloc="{}:{}".format(old.hostname, self.port),
                           path=old.path + self.group_prefix,
                           params=old.params,
                           query=old.query,
                           fragment=old.fragment).geturl()

    def _construct_topic_url(self, topics):
        """
        Construct the full URL, given a list of topics,
        or single topic.
        """

        if isinstance(topics, str):
            topics = [topics]

        url = urlparse(self.base_url_prefix)
        delimiter = ',' + url.path[1:] + '.'

        return ParseResult(scheme=url.scheme,
                           netloc=url.netloc,
                           path=url.path + '.' + delimiter.join(topics),
                           params=url.params,
                           query=url.query,
                           fragment=url.fragment).geturl()

    def listen(self, callback=None, topic=None):
        """
        Set a callback to be executed for each pubsub item received.

        Parameters
        ----------
        callback : callable (optional)
            A function of two arguments: the topic and the alert payload.
            When set to :obj:`None`, print out alert payload.
        topic : :obj:`str`, or :obj:`list` of :obj:`str` (optional)
            Topic or list of topics to listen to. When set to :obj:`None`,
            then listen to all topics connected to user's credential.
        """

        if topic:
            if isinstance(topic, str):
                topic = [topic]
            listen_topics = topic
        else:
            listen_topics = self.get_topics()

        with self.open(self._construct_topic_url(listen_topics), "r") as s:
            for payload, metadata in s.read(metadata=True,
                                            batch_size=self.batch_size,
                                            batch_timeout=self.batch_timeout):
                try:
                    payload = json.loads(payload)
                except (JSONDecodeError, TypeError) as e:
                    warnings.warn("Payload is not valid json: {}".format(e))

                if not callback:
                    print("New message from topic {topic}: \n {msg}\n"
                          .format(topic=metadata.topic, msg=payload))
                else:
                    callback(topic=metadata.topic.split('.')[1],
                             payload=payload)

    def connect(self, topics):
        """
        Takes in a topic or list of topics. Create writable
        stream objects for each of the topics in the list.

        Must have publish rights on topic.

        Parameters
        ----------
        topic : :obj:`str`, or :obj:`list` of :obj:`str`
            Topic or list of topics to publish to
        """

        if isinstance(topics, str):
            topics = [topics]

        # populate the session dict with new sessions:

        for topic in topics:
            self.sessions[topic] = self.open(self._construct_topic_url(topic),
                                             "w")

    def publish_to_topic(self, topic, msg):
        """
        Publish to a specific topic after a session
        has been connected with client.connect()

        Parameters
        ----------
        topic : :obj:`str`
            Topic name to publish to

        msg : :obj:`str`
            A message to publish to a topic

        """

        if not self.sessions:
            raise RuntimeError('No active sessions. Please '
                               'connect before publishing to a node.')

        # Write something:
        self.sessions[topic].write(msg)

    def disconnect(self, topics=None):
        """
        Close all the current stream, or optionally close a single
        or list of topics

        Parameters
        ----------
        topic : :obj:`str`, or :obj:`list` of :obj:`str` (optional)
            Topic or list of topics to disconnect from. If None, then
            disconnect from all topics.

        """

        if not self.sessions:
            raise UserWarning("No active sessions in progress")

        if not topics:
            for topic, session in self.sessions.items():
                session.close()
        else:
            if isinstance(topics, str):
                topics = [topics]
            for topic in topics:
                try:
                    self.session[topic].close()
                    self.session.pop(topic)
                except Exception:
                    raise UserWarning("Not currently connected to "
                                      "topic {}".format(topic))

    def publish(self, topic, msg=None):
        """
        Send an LVAlert without pre-establishing a session.

        Parameters
        ----------
        topic : :obj:`str`, or :obj:`list` of :obj:`str` (optional)
            Topic or list of topics to publish to.

        msg : :obj:`str`
            A message to publish to a topic
        """

        with self.open(self._construct_topic_url(topic), "w") as s:
            s.write(msg)

    def get_topics(self, group=None):
        """
        Get a list of all available pubsub nodes.

        Parameters
        ----------
        group : :obj:`str` (optional)
            Group prefix (e.g., "lvalert", "lvalert-playground") to show
            topics for. If :obj:`None`, list topics for the current group.

        """

        # Get the gracedb group from the argument, or from the
        # current session.

        if not group:
            group = self.group_prefix

        # Get the dict of topics from the server. convert the keys to a list.
        # Note: self.auth currently returns a list. FIXME: for now return the
        # first item in the list. Assumes only one credential, i guess.

        all_topics = list(list_topics(url=self.server,
                                      auth=self.auth[0]).keys())

        return [node.split('.')[1] for node in all_topics if
                group + '.' in node]

    def get_subscriptions(self):
        """
        Get a list of your subscriptions.
        """
        raise DeprecationWarning("This feature is deprecated. Please refer "
                                 "to the client.listen() method")

    def subscribe(self, *nodes):
        """
        Subscribe to one or more pubsub nodes.
        """
        raise DeprecationWarning("This feature is deprecated. Please supply"
                                 "list of topics to client.listen(), "
                                 "and ensure you have permission to read "
                                 "from topics.")

    def unsubscribe(self, *nodes):
        """
        Unsubscribe from one or more pubsub nodes.
        """
        raise DeprecationWarning("This feature is deprecated.")

    def delete(self):
        """
        Delete a pubsub topic
        """
        raise DeprecationWarning("This feature is deprecated.")
