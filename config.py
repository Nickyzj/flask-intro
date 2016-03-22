# default config
import os

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'my previous'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False 