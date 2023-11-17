from __future__ import annotations
import ntcore._ntcore.meta
import typing

__all__ = [
    "Client",
    "ClientPublisher",
    "ClientSubscriber",
    "SubscriberOptions",
    "TopicPublisher",
    "TopicSubscriber",
    "decodeClientPublishers",
    "decodeClientSubscribers",
    "decodeClients",
    "decodeTopicPublishers",
    "decodeTopicSubscribers"
]


class Client():
    """
    Client (as published via `$clients`).
    """
    def __init__(self) -> None: ...
    @property
    def conn(self) -> str:
        """
        :type: str
        """
    @conn.setter
    def conn(self, arg0: str) -> None:
        pass
    @property
    def id(self) -> str:
        """
        :type: str
        """
    @id.setter
    def id(self, arg0: str) -> None:
        pass
    @property
    def version(self) -> int:
        """
        :type: int
        """
    @version.setter
    def version(self, arg0: int) -> None:
        pass
    pass
class ClientPublisher():
    """
    Client publisher (as published via `$clientpub$<client>` or `$serverpub`).
    """
    def __init__(self) -> None: ...
    @property
    def topic(self) -> str:
        """
        :type: str
        """
    @topic.setter
    def topic(self, arg0: str) -> None:
        pass
    @property
    def uid(self) -> int:
        """
        :type: int
        """
    @uid.setter
    def uid(self, arg0: int) -> None:
        pass
    pass
class ClientSubscriber():
    """
    Client subscriber (as published via `$clientsub$<client>` or `$serversub`).
    """
    def __init__(self) -> None: ...
    @property
    def options(self) -> SubscriberOptions:
        """
        :type: SubscriberOptions
        """
    @options.setter
    def options(self, arg0: SubscriberOptions) -> None:
        pass
    @property
    def topics(self) -> typing.List[str]:
        """
        :type: typing.List[str]
        """
    @topics.setter
    def topics(self, arg0: typing.List[str]) -> None:
        pass
    @property
    def uid(self) -> int:
        """
        :type: int
        """
    @uid.setter
    def uid(self, arg0: int) -> None:
        pass
    pass
class SubscriberOptions():
    """
    Subscriber options. Different from PubSubOptions in this reflects only
    options that are sent over the network.
    """
    def __init__(self) -> None: ...
    @property
    def periodic(self) -> float:
        """
        :type: float
        """
    @periodic.setter
    def periodic(self, arg0: float) -> None:
        pass
    @property
    def prefixMatch(self) -> bool:
        """
        :type: bool
        """
    @prefixMatch.setter
    def prefixMatch(self, arg0: bool) -> None:
        pass
    @property
    def sendAll(self) -> bool:
        """
        :type: bool
        """
    @sendAll.setter
    def sendAll(self, arg0: bool) -> None:
        pass
    @property
    def topicsOnly(self) -> bool:
        """
        :type: bool
        """
    @topicsOnly.setter
    def topicsOnly(self, arg0: bool) -> None:
        pass
    pass
class TopicPublisher():
    """
    Topic publisher (as published via `$pub$<topic>`).
    """
    def __init__(self) -> None: ...
    @property
    def client(self) -> str:
        """
        :type: str
        """
    @client.setter
    def client(self, arg0: str) -> None:
        pass
    @property
    def pubuid(self) -> int:
        """
        :type: int
        """
    @pubuid.setter
    def pubuid(self, arg0: int) -> None:
        pass
    pass
class TopicSubscriber():
    """
    Topic subscriber (as published via `$sub$<topic>`).
    """
    def __init__(self) -> None: ...
    @property
    def client(self) -> str:
        """
        :type: str
        """
    @client.setter
    def client(self, arg0: str) -> None:
        pass
    @property
    def options(self) -> SubscriberOptions:
        """
        :type: SubscriberOptions
        """
    @options.setter
    def options(self, arg0: SubscriberOptions) -> None:
        pass
    @property
    def subuid(self) -> int:
        """
        :type: int
        """
    @subuid.setter
    def subuid(self, arg0: int) -> None:
        pass
    pass
def decodeClientPublishers(data: buffer) -> typing.Optional[typing.List[ClientPublisher]]:
    """
    Decodes `$clientpub$<topic>` meta-topic data.

    :param data: data contents

    :returns: Vector of ClientPublishers, or empty optional on decoding error.
    """
def decodeClientSubscribers(data: buffer) -> typing.Optional[typing.List[ClientSubscriber]]:
    """
    Decodes `$clientsub$<topic>` meta-topic data.

    :param data: data contents

    :returns: Vector of ClientSubscribers, or empty optional on decoding error.
    """
def decodeClients(data: buffer) -> typing.Optional[typing.List[Client]]:
    """
    Decodes `$clients` meta-topic data.

    :param data: data contents

    :returns: Vector of Clients, or empty optional on decoding error.
    """
def decodeTopicPublishers(data: buffer) -> typing.Optional[typing.List[TopicPublisher]]:
    """
    Decodes `$pub$<topic>` meta-topic data.

    :param data: data contents

    :returns: Vector of TopicPublishers, or empty optional on decoding error.
    """
def decodeTopicSubscribers(data: buffer) -> typing.Optional[typing.List[TopicSubscriber]]:
    """
    Decodes `$sub$<topic>` meta-topic data.

    :param data: data contents

    :returns: Vector of TopicSubscribers, or empty optional on decoding error.
    """
