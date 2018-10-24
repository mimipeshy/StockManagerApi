from flask import Flask

from instance.config import app_config
from app.api.v1.blueprint import ns as version1


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(app_config[config_name])
    # app.config.from_pyfile('config.py')

    app.register_blueprint(version1)
    return app
