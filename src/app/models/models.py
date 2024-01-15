from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "Users"
    name = db.Column(db.String(100), primary_key=True, nullable=False)
    password = db.Column(db.String(100), unique=False, nullable=False)
    notes = db.relationship("Note", backref="Users")

    def __init__(self, name, password):
        self.name = name
        self.password = password


class Note(db.Model):
    __tablename__ = "Notes"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), db.ForeignKey("Users.name"), nullable=False)
    title = db.Column(db.String(100), unique=False, nullable=False)
    text = db.Column(db.String(1000), unique=False, nullable=False)

    def __init__(self, username, title, text):
        self.username = username
        self.title = title
        self.text = text
