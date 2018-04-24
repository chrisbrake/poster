from flask import Blueprint, render_template, send_from_directory

web_mod = Blueprint('poster_web', __name__)


@web_mod.route('/')
def poster():
    """ Send an HTML page the user can interact with """
    return render_template('chat.html')


@web_mod.route('/static/<path:path>')
def static_files(path):
    """ Serve up static files from the static directory """
    return send_from_directory('static', path)
