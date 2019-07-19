import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'postgresql:///domains_analyzer'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDISTOGO_URL = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost"6379/0'
