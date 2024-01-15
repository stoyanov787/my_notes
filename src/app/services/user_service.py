import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.insert(0, parent)

from models.models import User


def get_users():
    users = User.query.all()
    users = {user.name: user.password for user in users}
    return users
