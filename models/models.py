import enum
from Utils.db import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields


# Relationships many to many
albums_songs = db.Table('album_song',
                        db.Column('album_id', db.Integer, db.ForeignKey('album.id'), primary_key=True),
                        db.Column('song_id', db.Integer, db.ForeignKey('song.id'), primary_key=True))


# Enums
class Medium(enum.Enum):
    DISCO = 1
    CASETE = 1
    CD = 3


# Models
class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    minutes = db.Column(db.Integer)
    seconds = db.Column(db.Integer)
    interpreter = db.Column(db.String(128))
    albums = db.relationship('Album', secondary='album_song', back_populates='songs')


class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(128))
    title = db.Column(db.String(128))
    medium = db.Column(db.Enum(Medium))
    year = db.Column(db.Integer)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    songs = db.relationship('Song', secondary='album_song', back_populates='albums')
    __table_args__ = (db.UniqueConstraint('user', 'title', name='title_uniq_album'),)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    password = db.Column(db.String(128))
    albums = db.relationship('Album', cascade='all, delete, delete-orphan')


# Serialization
class EnumADictionary(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return {'key': value.name, 'value': value.value}


class AlbumSchema(SQLAlchemyAutoSchema):
    medium = EnumADictionary(attribute='medium')
    class Meta:
        model = Album
        include_relationships = True
        load_instance = True


class SongSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Song
        include_relationships = True
        load_instance = True


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True
