import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///whisky_distillery.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True