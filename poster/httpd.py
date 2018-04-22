import gunicorn.app.base
from poster import app
from poster.log_init import log_maker

logger = log_maker()

gunicorn_config = [
    ('bind', '127.0.0.1:8080'),
    ('certfile', 'cert.pem'),
    ('forwarded_allow_ips', '*'),
    ('keyfile', 'key.pem'),
    ('secure_scheme_headers', {"X-FORWARDED-PROTO": "http"}),
    ('workers', 1),
]
# To Generate cert and key files:
# openssl req -x509 -newkey rsa:4096 -days 365 -nodes \
#   -keyout key.pem -out cert.pem


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
    WebApplication(app, gunicorn_config).run()


if __name__ == '__main__':
    main()
