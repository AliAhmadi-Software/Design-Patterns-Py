class Observer:
    def update(self, message):
        pass


class Channel:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def send_message(self, message):
        for observer in self.observers:
            observer.update(message)


class User(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received: {message}")


if __name__ == "__main__":
    chat_channel = Channel()
    user1 = User("Ali")
    user2 = User("Reza")

    chat_channel.add_observer(user1)
    chat_channel.add_observer(user2)

    chat_channel.send_message("Hello everyone!")
