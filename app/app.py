from flask import Flask
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_marshmallow import Marshmallow # type: ignore
from flask_cors import CORS # type: ignore

from app.config.db import Config

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)

  db.init_app(app)
  ma.init_app(app)
  
  CORS(app)

  with app.app_context():
    from .controllers.Event_controller import EventController
    db.create_all()

  return app