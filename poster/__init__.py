from flask import Flask
from poster.api.routes import api_mod
from poster.web.routes import web_mod

app = Flask(__name__)
app.register_blueprint(api_mod, url_prefix='/api/v1')
app.register_blueprint(web_mod)
