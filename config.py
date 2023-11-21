import os

class Config():
    SECRET_KEY = 'rfdsa89fyu9er4we5r34t4rgy546574845845yghetrgw8eyr322q3'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'core', 'core.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
