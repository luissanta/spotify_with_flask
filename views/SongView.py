from flask_restful import Resource
from models.models import Song, SongSchema
from flask import request
from Utils.db import db
from flask_jwt_extended import jwt_required

song_schema = SongSchema()

class SongsView(Resource):

    @classmethod
    @jwt_required()
    def get(cls):
        return [song_schema.dump(song) for song in Song.query.all()], 200

    @classmethod
    @jwt_required()
    def post(cls):
        new_song = Song(
            title=request.json['title'],
            minutes=request.json['minutes'],
            seconds=request.json['seconds'],
            interpreter=request.json['interpreter']
        )
        print(request)
        db.session.add(new_song)
        db.session.commit()
        return song_schema.dump(new_song), 201


class SongView(Resource):

    @classmethod
    @jwt_required()
    def get(cls, id_song):
        song = Song.query.get_or_404(id_song)
        return song_schema.dump(song), 200

    @classmethod
    @jwt_required()
    def put(cls, id_song):
        song = Song.query.get_or_404(id_song)
        song.title = request.json.get('title', song.title)
        song.minutes = request.json.get('minutes', song.minutes)
        song.seconds = request.json.get('seconds', song.seconds)
        song.interpreter = request.json.get('interpreter', song.interpreter)
        db.session.commit()
        return song_schema.dump(song), 201

    @classmethod
    @jwt_required()
    def delete(cls, id_song):
        song = Song.query.get_or_404(id_song)
        db.session.delete(song)
        db.session.commit()
        return song_schema.dump(song), 204
