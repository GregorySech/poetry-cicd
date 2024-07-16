from flask import Flask
from poetry_cicd import app


def create_app() -> Flask:
    return app
