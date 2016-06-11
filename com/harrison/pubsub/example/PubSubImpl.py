from com.harrison.pubsub.PubSubInterface import PubSubInterface


class PubSubImpl(PubSubInterface):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def receive(self, data):
        print("{} received {}".format(self.name, data))
