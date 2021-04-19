from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_moment import Moment

bootstrap = Bootstrap()
moment = Moment()


def create_app(config_name):
    app = Flask(__name__)

    #set up configurations
    app.config.from_object(config_options[config_name])

    #initialize app extensions
    bootstrap.init_app(app)
    moment.init_app(app)

    # Register the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config in request.py

    from .requests import configure_request
    configure_request(app)

    return app
