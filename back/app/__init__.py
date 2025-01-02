"""Initialisation de l'application Flask et des extensions."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .extensions import db
from .routes import api
from . import dict_extension
from . import extensions
from . import models
from . import repositories
from . import services

migrate = Migrate()

def create_app():
    """Crée et configure l'application Flask.

    Returns:
        Flask: L'application Flask configurée.
    """
    app = Flask(__name__)
    app.config.from_object('config.Config')

    app.register_blueprint(api, url_prefix='/v1')

    db.init_app(app)
    migrate.init_app(app, db)
    
    from app import models

    return app
