from flask.app import Flask
from flask.testing import FlaskCliRunner, FlaskClient
import pytest

from poetry_cicd import create_app


@pytest.fixture
def app():
    app = create_app()

    yield app


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


@pytest.fixture
def runner(app: Flask) -> FlaskCliRunner:
    return app.test_cli_runner()


def test_healthcheck(client: FlaskClient):
    response = client.get("/healthcheck")
    assert response.status_code == 200
