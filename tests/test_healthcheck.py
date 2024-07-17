from flask.testing import FlaskClient

from poetry_cicd import create_testable_app
from tests.fixtures import *


def test_healthcheck(client: FlaskClient):
    response = client.get("/healthcheck")
    assert response.status_code == 200
