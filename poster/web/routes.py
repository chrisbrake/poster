from flask import Blueprint, render_template, send_from_directory
from flask_login import login_required

web_mod = Blueprint('web', __name__)


@web_mod.route('/')
@login_required
def poster():
    """ Send an HTML page the user can interact with """
    return render_template('chat.html')


@web_mod.route('/static/<path:path>')
@login_required
def static_files(path):
    """ Serve up static files from the static directory """
    return send_from_directory('static', path)
