from datetime import datetime
import time

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

    def export(self):
        """
        Convert this object to a JSON string.
        :return: Dictionary representation of internal data.
        """
        return {
            'created': time.mktime(self.created.timetuple()),
            'modified': time.mktime(self.modified.timetuple()),
            'created_by': self.created_by,
            'channel': self.channel,
            'data': self.data
        }
