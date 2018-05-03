from flask import Flask
from flask_socketio import SocketIO, send
from poster.web import web_mod
from poster.log_init import log_maker

logger = log_maker()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Super Secret!'
app.register_blueprint(web_mod)
api_sio = SocketIO(app)

chat_data = ['Welcome']


@api_sio.on('connect')
def on_connect():
    """ Reply with a list of Channel data """
    logger.debug('Connection happened')
    send(chat_data, json=True)


@api_sio.on('chat')
def on_chat(chat):
    """ Reply with a list of Channel data """
    logger.debug('Got chat: ', chat)
    try:
        chat_data.append(chat['msg'])
        send(chat_data, json=True, broadcast=True)
    except KeyError:
        return


@api_sio.on('disconnect')
def on_disconnect():
    """ Reply with a list of Channel data """
    logger.debug('Disconnection happened')


if __name__ == '__main__':
    app.run(app)
