import gunicorn.app.base
from poster import app

gunicorn_config = [
    ('bind', '0.0.0.0:8080'),
    ('certfile', 'cert.pem'),
    ('forwarded_allow_ips', '*'),
    ('keyfile', 'key.pem'),
    ('secure_scheme_headers', {"X-FORWARDED-PROTO": "http"}),
    ('worker_class', 'eventlet')
]


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


def main():
    """
    The entry point into this application
    :return: None
    """
    app.debug = True
    WebApplication(app, gunicorn_config).run()


if __name__ == '__main__':
    main()
