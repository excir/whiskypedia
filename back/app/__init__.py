from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .extensions import db
from .routes import api

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    app.register_blueprint(api, url_prefix='/v1')

    db.init_app(app)
    migrate.init_app(app, db)

    return app
