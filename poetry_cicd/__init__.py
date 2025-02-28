from dataclasses import dataclass
from dotenv import load_dotenv
from flask import Flask, request
from flask.helpers import flash, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy


from poetry_cicd.contact import Base, Contact

load_dotenv()


def foo(x):
    return x + 1


def setup_db(app: Flask) -> SQLAlchemy:
    db = SQLAlchemy(model_class=Base)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return db


@dataclass
class Application:
    server: Flask
    db: SQLAlchemy


def create_testable_app() -> Application:

    server = Flask(__name__)
    server.config.from_prefixed_env("HTMCONTACTS")
    server.secret_key = server.config["SECRET_KEY"]

    db = setup_db(server)

    @server.route("/")
    def index():
        return redirect("/contact")

    @server.route("/healthcheck")
    def healthcheck():
        return render_template("healthcheck.html")

    @server.route("/contact")
    def contacts():
        search = request.args.get("q")
        if search is not None:
            contacts_set = Contact.search(db, search)
        else:
            contacts_set = Contact.all(db)
        return render_template("index.html", contacts=contacts_set)

    @server.route("/contact/new", methods=["GET"])
    def contacts_new_get():
        return render_template("new_contact.html", contact=Contact(), errors={})

    @server.route("/contact/new", methods=["POST"])
    def contacts_new_post():
        c = Contact(
            first=request.form["first_name"],
            last=request.form["last_name"],
            phone=request.form["phone"],
            email=request.form["email"],
        )
        try:
            db.session.add(c)
            db.session.commit()
            flash("Created new contact!")
            return redirect("/contact")
        except:
            return render_template("new_contact.html", contact=c, errors={})

    @server.route("/contact/<contact_id>")
    def contact_view(contact_id=0):
        contact = Contact.find(db, contact_id)
        return render_template("show.html", contact=contact)

    @server.route("/contact/<contact_id>/edit", methods=["GET"])
    def contact_edit_get(contact_id=0):
        contact = Contact.find(db, contact_id)
        return render_template("edit.html", contact=contact, errors={})

    @server.route("/contact/<contact_id>/edit", methods=["POST"])
    def contact_edit_post(contact_id=0):
        contact = Contact.find(db, contact_id)
        if contact is not None:
            contact.first = request.form["first_name"]
            contact.last = request.form["last_name"]
            contact.email = request.form["email"]
            contact.phone = request.form["phone"]
        db.session.merge(contact)
        try:
            db.session.commit()
            flash("Updated Contact!")
            return redirect(f"/contact/{contact_id}")
        except:
            return render_template("edit.html", contact=contact, errors={})

    @server.route("/contact/<contact_id>/delete", methods=["POST"])
    def contact_delete(contact_id=0):
        contact = Contact.find(db, contact_id)
        if contact is not None:
            contact.delete(db)
        db.session.commit()
        flash("Deleted Contact!")
        return redirect("/contact")

    return Application(server=server, db=db)


def create_app():
    app = create_testable_app()
    return app.server
