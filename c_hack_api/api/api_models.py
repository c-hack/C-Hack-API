"""
Module containing models for whole API to use.
"""

from flask_restplus import fields
from . import API
from ..db_models import STD_STRING_SIZE

ROOT_MODEL = API.model('RootModel', {

})
