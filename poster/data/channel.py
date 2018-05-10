from threading import Lock
from .message import Message


class Channel(object):
    """ An object to handle messages in a channel """

    def __init__(self, name):
        self.name = name
        self.lock = Lock()
        self._messages = list()
        self._observers = list()

    @property
    def messages(self):
        return [msg.export() for msg in self._messages]

    @property
    def new_message(self):
        return self._messages[-1]

    @new_message.setter
    def new_message(self, message):
        if not isinstance(message, Message):
            raise TypeError('message needs to be of Type Message.')
        self.lock.acquire()
        self._messages.append(message)
        for observer in self._observers:
            observer(self.messages)
        self.lock.release()

    def add_observer(self, observer):
        self._observers.append(observer)
