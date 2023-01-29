from flask_restful import Resource
from models.models import User, UserSchema
from flask import request
from Utils.db import db

user_schema = UserSchema()

class UsersView(Resource):

    @classmethod
    def get(cls):
        return [user_schema.dump(user) for user in User.query.all()]

    @classmethod
    def post(cls):
        new_user = User(
            name=request.json['name'],
            password=request.json['password']
        )
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user)


class UserView(Resource):

    @classmethod
    def put(cls, id_user):
        user = User.query.get_or_404(id_user)
        user.name = request.json.get('name', user.name)
        user.password = request.json.get('password', user.password)
        db.session.commit()
        return user_schema.dump(user)

    @classmethod
    def delete(cls, id_user):
        user = User.query.get_or_404(id_user)
        db.session.delete(user)
        db.session.commit()
        return user_schema.dump(user), 204
