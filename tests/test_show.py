from sqlalchemy import insert, select
from werkzeug.test import TestResponse
from poetry_cicd.contact import Contact
from tests.fixtures import *
from bs4 import BeautifulSoup


def test_show_contact_has_back_link(client: FlaskClient):

    response: TestResponse = client.get("/contact/1")
    assert response.status_code == 200
    soup = BeautifulSoup(response.text, "html.parser")

    back_links = soup.find_all(id="back-link")
    assert len(back_links) == 1


def test_show_contact_has_edit_link(
    client: FlaskClient, database: SQLAlchemy, server: Flask
):
    # Setup
    with server.app_context():
        contact = Contact()
        contact.first = "Pippo"
        contact.last = "Baudo"
        contact.email = "baudo@email"
        contact.phone = "ringring"
        database.session.add(contact)
        database.session.commit()
        contact = database.session.query(Contact).one()

    # Act
    response: TestResponse = client.get(f"/contact/{contact.id}")
    assert response.status_code == 200
    soup = BeautifulSoup(response.text, "html.parser")

    # Assert
    edit_links = soup.find_all(id="edit-link")
    assert len(edit_links) == 1
