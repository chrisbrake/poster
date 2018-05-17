from flask import Blueprint, request
from flask_restful import Api, Resource
from poster.data import rooms, Message
from poster.log_init import log_maker

logger = log_maker()
api_mod = Blueprint('api', __name__)
api = Api(api_mod)


class MessageResource(Resource):
    def get(self, room):
        return rooms[room].messages

    def post(self, room):
        data = request.json.get('data')
        creator = request.json.get('created_by')
        logger.debug('ReST Data: created_by %s, data %s' % (creator, data))
        rooms[room].new_message = Message(data=data, created_by=creator)


api.add_resource(MessageResource, '/Messages/<room>')
