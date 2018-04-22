from flask import Blueprint, send_from_directory

web_mod = Blueprint('poster_web', __name__)


@web_mod.route('/')
def poster():
    """ Send an HTML page the user can interact with """
    with open('static/chat.html', 'rb') as c:
        return c.read()


@web_mod.route('/static/<path:path>')
def static_files(path):
    return send_from_directory('static', path)
