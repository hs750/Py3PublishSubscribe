from abc import ABCMeta, abstractmethod
from com.harrison.pubsub.PubSubManager import PubSubManager


def class_fullname(clazz):
    """
    Gets the fully qualified class name of the parameter clazz
    :param clazz: Either a type or any object
    :return: the full name of the type or the type of the object
    """
    if clazz.__class__.__name__ == "type":
        return ".".join((clazz.__module__, clazz.__name__))
    else:
        return ".".join((clazz.__class__.__module__, clazz.__class__.__name__))


class PubSubInterface(metaclass=ABCMeta):
    pubSubManagers = dict()

    def __init__(self, loopback=False):
        self.allowPublishLoopback = loopback

    def subscribe(self, clazz):
        """
        Subscribe to a type.
        :param clazz: A type or an instance of the type to subscribe to
        :return: None
        """
        clazz = class_fullname(clazz)
        if clazz not in PubSubInterface.pubSubManagers:
            psm = PubSubManager(clazz)
            PubSubInterface.pubSubManagers[clazz] = psm
        else:
            psm = PubSubInterface.pubSubManagers[clazz]
        psm.add_subscriber(self)

    @abstractmethod
    def receive(self, data):
        pass

    def publish(self, data):
        if class_fullname(data) in PubSubInterface.pubSubManagers:
            psm = PubSubInterface.pubSubManagers[class_fullname(data)]
            psm.broadcast_data(data, self)

    def loopback_allowed(self):
        return self.allowPublishLoopback
