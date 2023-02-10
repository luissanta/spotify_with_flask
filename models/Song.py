from Utils.db import db
from models.Album import Album

albums_songs = db.Table('album_song',
                        db.Column('album_id', db.Integer, db.ForeignKey('album.id'), primary_key=True),
                        db.Column('song_id', db.Integer, db.ForeignKey('song.id'), primary_key=True))


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    minutes = db.Column(db.Integer)
    seconds = db.Column(db.Integer)
    interpreter = db.Column(db.String(128))
    albums = db.relationship(Album, secondary='album_song', back_populates='songs')
