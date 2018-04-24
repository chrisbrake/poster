from flask import Flask, jsonify, json
from flask_socketio import SocketIO, send
from poster.web import web_mod
from poster.log_init import log_maker

logger = log_maker()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Super Secret!'
app.register_blueprint(web_mod)
api_sio = SocketIO(app)

channel_data = {'main': ['Welcome to the main room.']}


@api_sio.on('json', namespace='api_v1')
def channels(json_data):
    """ Reply with a list of Channel data """
    logger.debug(json.dumps(json_data))
    send(jsonify(channel_data), json=True, room='main', broadcast=True)


if __name__ == '__main__':
    app.run(app)
