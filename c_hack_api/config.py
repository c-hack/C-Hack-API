"""Module containing default config values."""

from random import randint
import logging


class Config(object):
    DEBUG = False
    TESTING = False
    RESTPLUS_VALIDATE = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_UNIQUE_CONSTRAIN_FAIL = 'UNIQUE constraint failed'
    URI_BASE_PATH = '/'

    LOGGING_CONFIGS = ['logging_config.json']

    JSON_SORT_KEYS = False
    JSONIFY_PRETTYPRINT_REGULAR = False
    RESTPLUS_JSON = {'indent': None}

class ProductionConfig(Config):
    pass

class DebugConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

    LOGGING_CONFIGS = ['logging_config.json', 'logging_config_debug.json']

class TestingConfig(Config):
    TESTING = True
