from flask import Flask
from flask_socketio import SocketIO, send
from poster.web import web_mod
from poster.log_init import log_maker

logger = log_maker()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Super Secret!'
app.register_blueprint(web_mod)
api_sio = SocketIO(app)

channel_data = {'main': ['Welcome to the main room.']}


@api_sio.on('connect')
def on_connect():
    """ Reply with a list of Channel data """
    logger.debug('Connection happened')
    send(channel_data, json=True)


@api_sio.on('message')
def on_message(message):
    """ Reply with a list of Channel data """
    logger.debug('Got message: ', message)
    send(channel_data, json=True)


@api_sio.on('json')
def on_json(json):
    """ Reply with a list of Channel data """
    logger.debug('Got json: ', json)
    send(channel_data, json=True)


@api_sio.on('disconnect')
def on_disconnect():
    """ Reply with a list of Channel data """
    logger.debug('Disconnection happened')


if __name__ == '__main__':
    app.run(app)
