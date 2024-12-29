"""Modèles de la base de données pour l'application."""
import uuid
from app import db
from .dict_extension import DictExtension

class Distillery(db.Model, DictExtension):
    """Modèle représentant une distillerie."""

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    country_id = db.Column(db.String, db.ForeignKey('library.id'), nullable=False)
    notes = db.Column(db.Text, nullable=True)

    whiskies = db.relationship('Whisky', backref='distillery', lazy=True)
    country = db.relationship('Library', foreign_keys=[country_id])

class Negociant(db.Model, DictExtension):
    """Modèle représentant un négociant."""

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    country_id = db.Column(db.String, db.ForeignKey('library.id'), nullable=True)
    notes = db.Column(db.Text, nullable=True)

    whiskies = db.relationship('Whisky', backref='negociant', lazy=True)
    country = db.relationship('Library', foreign_keys=[country_id])

class Whisky(db.Model, DictExtension):
    """Modèle représentant un whisky."""

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    distillery_id = db.Column(db.String, db.ForeignKey('distillery.id'), nullable=False)
    negociant_id = db.Column(db.String, db.ForeignKey('negociant.id'), nullable=True)
    alcohol_percentage = db.Column(db.Float, nullable=False)
    whisky_type_id = db.Column(db.String, db.ForeignKey('library.id'), nullable=False)
    bottle_size_cl = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    is_peated = db.Column(db.Boolean, nullable=False, default=False)
    nose = db.Column(db.Text, nullable=True)
    appearance = db.Column(db.Text, nullable=True)
    palate = db.Column(db.Text, nullable=True)
    finish = db.Column(db.Text, nullable=True)
    photo = db.Column(db.String, nullable=True)

    tastings = db.relationship('Tasting', backref='whisky', lazy=True, cascade='all, delete-orphan')
    whisky_type = db.relationship('Library', foreign_keys=[whisky_type_id])

class Tasting(db.Model, DictExtension):
    """Modèle représentant une dégustation."""

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    whisky_id = db.Column(db.String, db.ForeignKey('whisky.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    tasting_date = db.Column(db.Date, nullable=False)

class Library(db.Model, DictExtension):
    """Modèle représentant une bibliothèque de data."""

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    data = db.Column(db.String(100), nullable=False)