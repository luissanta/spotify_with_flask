from Utils.db import db
from index import create_app
from flask_restful import Api
from views.SongView import SongsView, SongView
from views.AlbumView import AlbumsView, AlbumView
from views.UserView import UsersView, UserView


app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(SongsView, '/songs')
api.add_resource(SongView, '/song/<int:id_song>')
api.add_resource(UsersView, '/users')
api.add_resource(UserView, '/user/<int:id_user>')
api.add_resource(AlbumsView, '/albums')
api.add_resource(AlbumView, '/album/<int:id_album>')
