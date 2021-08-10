import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDISTOGO_URL = os.getenv('REDISTOGO_URL', 'redis://redis:6379')
    CELERY_BROKER_URL = 'redis://redis:6379/0'
    CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
    CELERY_WORKER = os.getenv('CELERY_WORKER', 'test')