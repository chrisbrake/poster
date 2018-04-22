from flask import Blueprint, request, jsonify

api_mod = Blueprint('poster_api', __name__)

channel_data = {'main': ['Welcome to the main room.']}


@api_mod.route('/')
def root():
    return jsonify({'version': '1.0.0'})


@api_mod.route('/channels/')
def channels():
    """ Reply with a list of Channels """
    return jsonify(list(channel_data.keys()))


@api_mod.route('/channels/<name>', methods=['GET', 'POST'])
def channel(name):
    """ Reply with a list of Channel data """
    if request.method == 'POST':
        if name not in channel_data:
            channel_data[name] = list()
        posted_data = request.get_json()
        channel_data[name].append(posted_data.get('message'))
        return jsonify('OK')
    elif request.method == 'GET':
        return jsonify(channel_data.get(name))
