import json
from datetime import datetime


class Message(object):
    """
    A class used to store a chat message
    """
    def __init__(self, created_by, data, channel=None):
        self.created = datetime.now()
        self.modified = datetime.now()
        self.created_by = created_by
        self.channel = channel
        self.data = data

    def as_json(self):
        """
        Convert this object to a JSON string.
        :return: String, formatted as JSON.
        """
        return json.dumps({
            'created': self.created.timestamp(),
            'modified': self.modified.timestamp(),
            'created_by': self.created_by.id,
            'channel': self.channel,
            'data': self.data
        })
