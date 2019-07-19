from flask import Flask
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from celery import Celery

DEBUG = False
app = Flask(__name__, static_folder='../templates/static', template_folder='../templates')
app.config.from_object(Config)
CORS(app, resources={r'/*': {'origins': '*'}}, expose_headers='Location')
celery = Celery(app.name, backend='redis', broker=app.config['CELERY_BROKER_URL'])


db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models