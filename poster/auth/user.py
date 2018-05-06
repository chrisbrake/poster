from flask_login import UserMixin


class User(UserMixin):
    """ User representation """


users = {'foo': {'password': 'bar'}}
