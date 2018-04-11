import falcon
import gunicorn.app.base
import os
from log_init import log_maker

gunicorn_config = [('bind', '127.0.0.1:8080'), ('workers', 1)]
channel_data = {'main': ['Welcome to the main room.']}
logger = log_maker()


class WebApplication(gunicorn.app.base.BaseApplication):
    """ The server that powers this application """
    def __init__(self, app, options):
        self.options = options
        self.application = app
        super(WebApplication, self).__init__()

    def load_config(self):
        for key, value in self.options:
            self.cfg.set(key, value)

    def load(self):
        return self.application

    def init(self, parser, opts, args):
        pass


class Poster(object):
    """ The main page of this application """
    def on_get(self, _, resp):
        """ Send an HTML page the user can interact with """
        with open('static/chat.html', 'rb') as c:
            resp.body = c.read()
        resp.content_type = falcon.MEDIA_HTML
        resp.status = falcon.HTTP_200


class Channels(object):
    """ Segmented chat areas """
    def on_get(self, _, resp):
        """ Reply with a list of Channels """
        channels = list(channel_data.keys())
        resp.media = channels
        resp.status = falcon.HTTP_200
        logger.debug('Channel List Request, returning: %s' % channels)


class Channel(object):
    """ A segment where a chat can take place """
    def on_get(self, _, resp, name):
        """ Reply with a list of Channel data """
        resp.media = channel_data.get(name)
        resp.status = falcon.HTTP_200
        logger.debug(
            'Channel %s Request, returning: %s' % name, channel_data.get(name))

    def on_post(self, req, resp, name):
        """ Add posted data to channel, creating it as needed """
        if name not in channel_data:
            channel_data[name] = list()
        channel_data[name].append(req.media)
        resp.status = falcon.HTTP_200
        logger.debug(
            'Channel %s Post: %s' % name, req.media)


def main():
    """
    The entry point into this application
    :return: None
    """
    api = falcon.API()
    api.add_route('/', Poster())
    api.add_route('/channels', Channels())
    api.add_route('/channels/{name}', Channel())
    api.add_static_route('/static', os.path.abspath('static'))
    WebApplication(api, gunicorn_config).run()


if __name__ == '__main__':
    main()
