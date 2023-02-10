from Utils.db import db
from flask_restful import Api
from views.SongView import SongsView, SongView
from views.AlbumView import AlbumsView, AlbumView
from views.UserView import UsersView, UserView
from flask import Flask
from config import DevelopmentConfig
from helpers.Errors import Errors
import unittest

app = Flask(__name__)
app_context = app.app_context()
app_context.push()

app.config.from_object(DevelopmentConfig)
db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(SongsView, '/songs')
api.add_resource(SongView, '/song/<int:id_song>')
api.add_resource(UsersView, '/users')
api.add_resource(UserView, '/user/<int:id_user>')
api.add_resource(AlbumsView, '/albums')
api.add_resource(AlbumView, '/album/<int:id_album>')


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)
    return app


if __name__ == '__main__':
    # Error handlers
    app.register_error_handler(404, Errors.page_not_found)
    app.register_error_handler(405, Errors.method_not_allowed)
    app.register_error_handler(500, Errors.server_error)

    app.run()
