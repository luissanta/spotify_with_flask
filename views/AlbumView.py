from flask_restful import Resource
from models.models import Album, AlbumSchema
from flask import request
from Utils.db import db

album_schema = AlbumSchema()

class AlbumsView(Resource):

    @classmethod
    def get(cls):
        return [album_schema.dump(album) for album in Album.query.all()]

    @classmethod
    def post(cls):
        new_album = Album(
            description=request.json['description'],
            title=request.json['title'],
            medium=request.json['medium'],
            year=request.json['year'],
        )
        db.session.add(new_album)
        db.session.commit()
        return album_schema.dump(new_album)


class AlbumView(Resource):

    @classmethod
    def put(cls, id_album):
        album = Album.query.get_or_404(id_album)
        album.description = request.json.get('description', album.description)
        album.title = request.json.get('title', album.title)
        album.medium = request.json.get('medium', album.medium)
        album.year = request.json.get('year', album.year)
        db.session.commit()
        return album_schema.dump(album)

    @classmethod
    def delete(cls, id_album):
        album = Album.query.get_or_404(id_album)
        db.session.delete(album)
        db.session.commit()
        return album_schema.dump(album), 204
