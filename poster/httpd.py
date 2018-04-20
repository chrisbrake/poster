import flask
import gunicorn.app.base
from poster.log_init import log_maker

logger = log_maker()
app = flask.Flask(__name__)
gunicorn_config = [('bind', '127.0.0.1:8080'), ('workers', 1)]
channel_data = {'main': ['Welcome to the main room.']}


class WebApplication(gunicorn.app.base.BaseApplication):
    """ The server that powers this application """
    def __init__(self, application, options):
        self.options = options
        self.application = application
        super(WebApplication, self).__init__()

    def load_config(self):
        for key, value in self.options:
            self.cfg.set(key, value)

    def load(self):
        return self.application

    def init(self, parser, opts, args):
        pass


@app.route('/')
def poster():
    """ Send an HTML page the user can interact with """
    with open('static/chat.html', 'rb') as c:
        return c.read()


@app.route('/channels/')
def channels():
    """ Reply with a list of Channels """
    return flask.jsonify(list(channel_data.keys()))


@app.route('/channels/<name>', methods=['GET', 'POST'])
def channel(name):
    """ Reply with a list of Channel data """
    if flask.request.method == 'POST':
        if name not in channel_data:
            channel_data[name] = list()
        posted_data = flask.request.get_json()
        channel_data[name].append(posted_data.get('message'))
        return flask.jsonify('OK')
    elif flask.request.method == 'GET':
        return flask.jsonify(channel_data.get(name))


@app.route('/static/<path:path>')
def static_files(path):
    return flask.send_from_directory('static', path)


def main():
    """
    The entry point into this application
    :return: None
    """
    WebApplication(app, gunicorn_config).run()


if __name__ == '__main__':
    main()
