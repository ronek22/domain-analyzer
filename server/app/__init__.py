from flask import Flask
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

DEBUG = True

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, resources={r'/*': {'origins': '*'}})
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models