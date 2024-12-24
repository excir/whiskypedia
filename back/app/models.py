import uuid
from sqlalchemy.dialects.postgresql import UUID
from app import db
from .dict_extension import DictExtension

class Distillery(db.Model, DictExtension):
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    notes = db.Column(db.Text, nullable=True)

    whiskies = db.relationship('Whisky', backref='distillery', lazy=True)

class Negotiant(db.Model, DictExtension):
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(50), nullable=True)
    notes = db.Column(db.Text, nullable=True)

    whiskies = db.relationship('Whisky', backref='negotiant', lazy=True)

class Whisky(db.Model, DictExtension):
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    distillery_id = db.Column(db.String, db.ForeignKey('distillery.id'), nullable=False)
    negotiant_id = db.Column(db.String, db.ForeignKey('negotiant.id'), nullable=True)
    alcohol_percentage = db.Column(db.Float, nullable=False)
    whisky_type = db.Column(db.String(50), nullable=False)
    bottle_size_cl = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    is_peated = db.Column(db.Boolean, nullable=False, default=False)
    nose = db.Column(db.Text, nullable=True)
    appearance = db.Column(db.Text, nullable=True)
    palate = db.Column(db.Text, nullable=True)
    finish = db.Column(db.Text, nullable=True)
    photo = db.Column(db.String, nullable=True)

    tastings = db.relationship('Tasting', backref='whisky', lazy=True)

class Tasting(db.Model, DictExtension):
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    whisky_id = db.Column(db.String, db.ForeignKey('whisky.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    tasting_date = db.Column(db.Date, nullable=False)
