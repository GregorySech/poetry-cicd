from flask import Flask, request
from flask.helpers import flash, redirect
from flask.templating import render_template

from poetry_cicd.contact import Contact


def foo(x):
    return x + 1


def create_app() -> Flask:
    app = Flask(__name__)
    app.secret_key = "lalla"

    @app.route("/")
    def index():
        return redirect("/contacts")

    @app.route("/healthcheck")
    def healthcheck():
        return render_template("healthcheck.html")

    @app.route("/contacts")
    def contacts():
        search = request.args.get("q")
        if search is not None:
            contacts_set = Contact.search(search)
        else:
            contacts_set = Contact.all()
        return render_template("index.html", contacts=contacts_set)

    @app.route("/contact/new", methods=["GET"])
    def contacts_new_get():
        return render_template("new_contact.html", contact=Contact())

    @app.route("/contact/new", methods=["POST"])
    def contacts_new_post():
        c = Contact(
            first=request.form["first_name"],
            last=request.form["last_name"],
            phone=request.form["phone"],
            email=request.form["email"],
        )

        if c.save():
            flash("Created new contact!")
            return redirect("/contacts")
        else:
            return render_template("new_contact.html", contact=c)

    return app
