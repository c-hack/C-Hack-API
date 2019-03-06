"""
Main API Module
"""
from typing import List
from functools import wraps
from flask import Blueprint
from flask_restplus import Api, Resource, abort, marshal
from .. import APP
API_BLUEPRINT = Blueprint('api', __name__)

def render_root(self):
    return self.make_response(marshal({}, ROOT_MODEL), 200)

Api.render_root = render_root
Api.base_path = APP.config['URI_BASE_PATH']

API = Api(API_BLUEPRINT, version='0.1', title='C-Hack API', doc='/doc/',
          description='The C-Hack API.', endpoint=APP.config['URI_BASE_PATH'])

# pylint: disable=C0413
from .api_models import ROOT_MODEL



@API.errorhandler
def default_errorhandler(error):
    """
    Handler function for a logging all errors
    """
    #APP.logger.exception()
    return {'message': error.message}, 500


APP.register_blueprint(API_BLUEPRINT, url_prefix='')

ROOT_NS = API.namespace('default', path='/')

@ROOT_NS.route('/')
class RootResource(Resource):
    """
    The API root element
    """

    @API.doc(security=None)
    @API.marshal_with(ROOT_MODEL)
    # pylint: disable=R0201
    def get(self):
        """
        Get the root element
        """
        print('HI')
        return None

API.render_root = RootResource.get

from . import open_close