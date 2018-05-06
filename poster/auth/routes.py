from flask import (
    Blueprint, render_template, request, redirect, url_for)
from flask_login import (
    current_user, login_required, login_user, logout_user)

from poster.auth import User, users

auth_mod = Blueprint('auth', __name__)


@auth_mod.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    name = request.form['uname']
    if request.form['password'] == users[name]['password']:
        user = User()
        user.id = name
        login_user(user)
        return redirect(url_for('web.poster'))

    return 'Bad login', 401


@auth_mod.route('/protected')
@login_required
def protected():
    return 'Logged in as: ' + current_user.id


@auth_mod.route('/logout')
def logout():
    logout_user()
    return 'Logged out'
