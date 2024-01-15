import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.insert(0, parent)

from flask import redirect, request
from models.models import Note, User, db
from services.note_service import get_notes
from services.user_service import get_users


def sign_up():
    if request.method == "GET":
        return """<form method="POST" action="">
        Name <input types="text" name="name">
        Password <input type="text" name="password">
        <input type="submit" value="Sign up">
        </form>"""

    name = request.form.get("name")
    password = request.form.get("password")

    if not name:
        return f"<h1>Name: {name} is not a valid name</h1>"
    if name in get_users():
        return f"<h1>Name: {name} is not available</h1>"
    if not password:
        return f"<h1>Password: {password} is not a valid password</h1>"

    user = User(name, password)
    db.session.add(user)
    db.session.commit()

    return redirect(f"/notes/{name}")


def log_in():
    if request.method == "GET":
        return """<form method="POST" action="">
        Name <input types="text" name="name">
        Password <input type="text" name="password">
        <input type="submit" value="Log in">
        </form>"""

    name = request.form.get("name")
    password = request.form.get("password")

    if not name in get_users():
        return f"<h1>Name: {name} does not exist</h1>"
    if not password == get_users()[name]:
        return f"<h1>Password: {password} is incorrect</h1>"

    return redirect(f"/notes/{name}")


def notes_options(name):
    return f"""<input type="button" value="Add a note" onclick="window.location = '/add_notes/{name}';">
            <input type="button" value="List the notes" onclick="window.location = '/list_notes/{name}';">"""


def add_notes(name):
    if request.method == "GET":
        return """<form method="POST" action="">
        Title <input type="text" name="title" required minlength="1" maxlength="100">
        Text <input type="text" name="text" required minlength="1" maxlength="100">
        <input type="submit" value="Add the note">
        </form>"""

    title = request.form.get("title")
    text = request.form.get("text")

    if not name in get_users():
        return f"<h1>Name: {name} does not exist</h1>"
    if not (0 < len(title) <= 100):
        return f"<h1>Title: {title} is not within the range of 1 to 100 characters</h1>"
    if not (0 < len(text) <= 1000):
        return f"<h1>Text: {text} is not within the range of 1 to 1000 characters</h1>"

    note = Note(name, title, text)
    db.session.add(note)
    db.session.commit()

    return redirect(f"/notes/{name}")


def list_notes(name):
    notes = get_notes()
    notes = {key: value for key, value in notes.items() if value["username"] == name}
    return notes


def list_users():
    return get_users()
