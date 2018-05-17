from flask import Flask
from flask_login import LoginManager, current_user
from flask_socketio import SocketIO, emit, disconnect, join_room, leave_room
from poster.api import api_mod
from poster.auth import auth_mod, User, users
from poster.data import Room, rooms, Message
from poster.web import web_mod
from poster.log_init import log_maker

logger = log_maker()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Super Secret!'
app.register_blueprint(web_mod)
app.register_blueprint(auth_mod, url_prefix='/auth')
app.register_blueprint(api_mod, url_prefix='/api')
api_sio = SocketIO(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'


def room_observer(room, message):
    logger.debug('observed a new message: %s' % message)
    api_sio.emit('chat', message, room=room, json=True)


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


@api_sio.on('chat')
def on_chat(chat):
    """ Actions to perform when a new chat message arrives """
    logger.debug('Got chat: %s' % chat)
    try:
        msg = chat['msg']
        room = chat['room']
        if room not in rooms:
            rooms[room] = Room(room)
            rooms[room].add_observer(room_observer)
        rooms[room].new_message = Message(created_by=current_user.id, data=msg)
    except KeyError:
        return


@api_sio.on('join')
def on_join(data):
    """ Actions to be performed when a client requests to join a room """
    room = data['room']
    join_room(room)
    on_chat({'msg': current_user.id + ' has entered ' + room, 'room': room})


@api_sio.on('leave')
def on_leave(data):
    """ Actions to be performed when a client requests to leave a room """
    room = data['room']
    leave_room(room)
    on_chat({'msg': current_user.id + ' has left ' + room})


@api_sio.on('disconnect')
def on_disconnect():
    """ Actions to perform when a disconnect occurs """
    logger.debug('Disconnection happened')


if __name__ == '__main__':
    app.run(app)
