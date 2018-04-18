"""
@Created by Seven on 2018-04-17
import os
from flask import (Flask,request....)
"""
from .config import configs

from flask import Flask


def register_blueprints(app):
    from .apps import book
    app.register_blueprint(book)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))

    register_blueprints(app)  # 注册路由

    return app
