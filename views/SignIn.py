from flask_restful import Resource
from models.models import User, UserSchema
from flask import request
from Utils.db import db
from flask_jwt_extended import create_access_token

user_schema = UserSchema()

class SignInView(Resource):
    @classmethod
    def post(cls):
        new_user = User(
            name=request.json['name'],
            password=request.json['password']
        )
        token = create_access_token(identity=request.json['name'])
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User created', 'token': token}

    @classmethod
    def put(cls, id_user):
        user = User.query.get_or_404(id_user)
        user.name = request.json.get('name', user.name)
        user.password = request.json.get('password', user.password)
        db.session.commit()
        return user_schema.dump(user)
