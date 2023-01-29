import enum
from Utils.db import db
from models.Song import Song


class Medium(enum.Enum):
    DISCO = 1
    CASETE = 1
    CD = 3


class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(128))
    title = db.Column(db.String(128))
    medium = db.Column(db.Enum(Medium))
    year = db.Column(db.Integer)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    songs = db.relationship(Song, secondary='album_song', back_populates='albums')
    __table_args__ = (db.UniqueConstraint('user', 'title', name='title_uniq_album'))
