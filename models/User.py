from Utils.db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    password = db.Column(db.String(128))
    albums = db.relationship('Album', cascade='all, delete, delete-orphan')
