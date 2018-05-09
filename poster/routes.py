from flask import Flask
from flask_login import LoginManager, current_user
from flask_socketio import SocketIO, emit, disconnect
from poster.auth import auth_mod, User, users
from poster.data import Channel, Message
from poster.web import web_mod
from poster.log_init import log_maker

logger = log_maker()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Super Secret!'
app.register_blueprint(web_mod)
app.register_blueprint(auth_mod, url_prefix='/auth')
api_sio = SocketIO(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'


def channel_observer(message):
    logger.debug('observed a new message: %s' % message)
    emit('chat', message, json=True, broadcast=True)


Channels = dict()
Channels['main'] = Channel('main')
Channels['main'].add_observer(channel_observer)


@login_manager.user_loader
def user_loader(name):
    if name not in users:
        return

    user = User()
    user.id = name
    return user


@login_manager.request_loader
def request_loader(request):
    name = request.form.get('name')
    if name not in users:
        return

    user = User()
    user.id = name
    user.is_authenticated = request.form['password'] == users[name]['password']

    return user


@api_sio.on('connect')
def on_connect():
    if not current_user.is_authenticated:
        disconnect()
    """ Actions to perform when a new client connects """
    logger.debug('Connection happened')
    emit('chat', Channels['main'].messages, json=True)


@api_sio.on('chat')
def on_chat(chat):
    """ Actions to perform when a new chat message arrives """
    logger.debug('Got chat: %s' % chat)
    try:
        msg = chat['msg']
        if not msg:
            return
        Channels['main'].new_message = msg
    except KeyError:
        return


@api_sio.on('disconnect')
def on_disconnect():
    """ Actions to perform when a disconnect occurs """
    logger.debug('Disconnection happened')


if __name__ == '__main__':
    app.run(app)
