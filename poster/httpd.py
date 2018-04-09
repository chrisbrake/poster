import falcon
import gunicorn.app.base
from cerberus import Validator


gunicorn_config = [('bind', '127.0.0.1:8080'), ('workers', 1)]
validator_schema = {'name': {'type': 'string', 'required': True},
                    'age': {'type': 'integer'}}
with open('chat.html') as c:
    chat_page = c.read()


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


class RootResource(object):

    def __init__(self):
        self.items = ['test']
        self.validator = Validator(validator_schema, allow_unknown=True)

    def on_get(self, _, response):
        """ Send an HTML page the user can interact with """
        response.body = chat_page
        response.content_type = 'text/html'
        response.status = falcon.HTTP_200

    def on_post(self, request, response):
        """ Accept chat messages """
        data = request.media
        if not self.validator.validate(data):
            response.status = falcon.HTTP_400
            response.media = self.validator.errors
            return
        self.items.append(data)
        response.status = falcon.HTTP_200
        response.body = 'Thank you'


def main():
    api = falcon.API()
    api.add_route('/', RootResource())
    WebApplication(api, gunicorn_config).run()


if __name__ == '__main__':
    main()
