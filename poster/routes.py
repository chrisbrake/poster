from flask import Flask
from flask_socketio import SocketIO, emit
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
    """ Actions to perform when a new client connects """
    logger.debug('Connection happened')
    emit('chat', chat_data, json=True)


@api_sio.on('chat')
def on_chat(chat):
    """ Actions to perform when a new chat message arrives """
    logger.debug('Got chat: %s' % chat)
    try:
        msg = chat['msg']
        if not msg:
            return
        chat_data.append(msg)
        emit('chat', chat_data, json=True, broadcast=True)
    except KeyError:
        return


@api_sio.on('disconnect')
def on_disconnect():
    """ Actions to perform when a disconnect occurs """
    logger.debug('Disconnection happened')


if __name__ == '__main__':
    app.run(app)
