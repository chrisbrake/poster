from flask import Blueprint
from flask_restful import Api, Resource, reqparse, fields
from ..data import Channels, Message

api_mod = Blueprint('api', __name__)
api = Api(api_mod)

post_parser = reqparse.RequestParser()
post_parser.add_argument(
    'data', dest='data', type=fields.String, location='form', required=True,
    help='The contents of the message',
)
post_parser.add_argument(
    'created_by', dest='created_by', type=fields.String, location='form',
    default='unknown', help='The username associated with message creation',
)


class MessageResource(Resource):
    def get(self, channel):
        return Channels[channel].messages

    def post(self, channel):
        args = post_parser.parse_args()
        Channels[channel].new_message = Message(
            data=args.get('data'), created_by=args.get('created_by'))


api.add_resource(MessageResource, '/Messages/<channel>')
