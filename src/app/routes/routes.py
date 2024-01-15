import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.insert(0, parent)

from controllers.controllers import (
    add_notes,
    list_notes,
    list_users,
    log_in,
    notes_options,
    sign_up,
)
from flask import Blueprint
from views.views import main

blueprint = Blueprint("blueprint", __name__)
blueprint.route("/", methods=["GET"])(main)
blueprint.route("/sign_up", methods=["GET", "POST"])(sign_up)
blueprint.route("/log_in", methods=["GET", "POST"])(log_in)
blueprint.route("/notes/<name>", methods=["GET"])(notes_options)
blueprint.route("/add_notes/<name>", methods=["GET", "POST"])(add_notes)
blueprint.route("/list_notes/<name>", methods=["GET"])(list_notes)
blueprint.route("/users", methods=["GET"])(list_users)
