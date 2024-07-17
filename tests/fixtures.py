from flask import Flask
from flask.testing import FlaskCliRunner, FlaskClient
from flask_sqlalchemy.extension import SQLAlchemy
import pytest
import os
from poetry_cicd import Application, create_testable_app
import time


@pytest.fixture
def application():
    os.environ["HTMCONTACTS_SQLALCHEMY_DATABASE_URI"] = (
        f"sqlite:///contacts-{time.time_ns()}.db"
    )
    app = create_testable_app()
    yield app


@pytest.fixture
def client(application: Application) -> FlaskClient:
    return application.server.test_client()


@pytest.fixture
def database(application: Application) -> SQLAlchemy:
    return application.db


@pytest.fixture
def server(application: Application) -> Flask:
    return application.server


@pytest.fixture
def runner(application: Application) -> FlaskCliRunner:
    return application.server.test_cli_runner()
