from flask import Flask
from poetry_cicd import app


def create_app() -> Flask:
    app = Flask(__name__)

    return app
