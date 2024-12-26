"""Configuration de l'application Flask."""

class Config:
    """Configuration de l'application Flask."""

    SQLALCHEMY_DATABASE_URI = 'sqlite:///whisky_distillery.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
