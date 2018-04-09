import falcon
import gunicorn.app.base

gunicorn_config = [('bind', '127.0.0.1:8080'), ('workers', 1)]
messages = list()


class WebApplication(gunicorn.app.base.BaseApplication):

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

    def on_get(self, _, response):
        """ Send an HTML page the user can interact with """
        with open('chat.html') as c:
            response.body = c.read()
        response.content_type = 'text/html'
        response.status = falcon.HTTP_200


class Messages(object):

    def on_post(self, request, response):
        """ Accept chat messages """
        data = request.stream.read().decode("UTF-8")
        messages.append(data)
        response.status = falcon.HTTP_200

    def on_get(self, _, response):
        """ Send chat messages """
        response.media = messages
        response.status = falcon.HTTP_200


def main():
    api = falcon.API()
    api.add_route('/', Poster())
    api.add_route('/msgs', Messages())
    WebApplication(api, gunicorn_config).run()


if __name__ == '__main__':
    main()
