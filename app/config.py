# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'HEqzrcjFMW5v'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://Nightcloud:09Pkb44wbqw!@localhost:3306/serenity_studio_database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
