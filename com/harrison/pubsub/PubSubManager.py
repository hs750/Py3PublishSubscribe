

class PubSubManager:

    def __init__(self, clazz):
        self.manages = clazz
        self.subscribers = set()

    def add_subscriber(self, subscriber):
        self.subscribers.add(subscriber)

    def broadcast_data(self, data, sender):
        for sub in self.subscribers:
            if sender is sub:
                if sender.loopback_allowed():
                    sub.receive(data)
            else:
                sub.receive(data)
