import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.insert(0, parent)

from models.models import Note


def get_notes():
    notes = Note.query.all()
    notes = {
        note.id: {
            "username": note.username,
            "title": note.title,
            "text": note.text,
        }
        for note in notes
    }
    return notes
