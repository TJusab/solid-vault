from flask import Flask
import os


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.add_url_rule('/', 'index')

    return app
