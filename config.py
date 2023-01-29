from decouple import config


class Config:
    SECRET_KEY = config('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATION = config('SQLALCHEMY_TRACK_MODIFICATION')


class DevelopmentConfig(Config):
    DEBUG = True
