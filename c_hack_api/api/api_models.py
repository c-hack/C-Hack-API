"""
Module containing models for whole API to use.
"""

from flask_restplus import fields
from . import API
from ..db_models import STD_STRING_SIZE

ROOT_MODEL = API.model('RootModel', {
    'openClose': fields.Url('api.openclose_period_list'),
})

OPEN_CLOSE_POST = API.model('OpenClosePOST', {
    'begin': fields.Integer(title='Open From'),
    'end': fields.Integer(title='Open Until'),
    'comment': fields.String(max_length=STD_STRING_SIZE,title='Comment'),
})

OPEN_CLOSE_GET = API.inherit('OpenCloseGET', OPEN_CLOSE_POST, {
    'id': fields.Integer(min=1, example=1, readonly=True, title='Internal Identifier'),
})

OPEN_CLOSE_PUT = API.inherit('OpenClosePUT', OPEN_CLOSE_POST, {})

