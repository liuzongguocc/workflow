import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SECRET_KEY="123"
    SQLALCHEMY_TRACK_MODIFICATIONS = False