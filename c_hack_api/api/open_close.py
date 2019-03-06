from flask import request
from flask_restplus import Api, Resource, abort, marshal
from sqlalchemy.exc import IntegrityError

from . import API
from . import APP
from .api_models import OPEN_CLOSE_GET
from .api_models import OPEN_CLOSE_POST
from .api_models import OPEN_CLOSE_PUT

from .. import DB
from ..db_models.open_close import OpenClose


OPEN_CLOSE_NS = API.namespace('openclose', description='OpenClose Endpoint', path='/open-close')

@OPEN_CLOSE_NS.route('/')
class PeriodList(Resource):
    """
    List of all periods
    """

    @API.marshal_list_with(OPEN_CLOSE_GET)
    # pylint: disable=R0201
    def get(self):
        """
        Get a list of all periods currently in the system
        """
        return OpenClose.query.all()

    @OPEN_CLOSE_NS.doc(model=OPEN_CLOSE_GET, body=OPEN_CLOSE_POST)
    @OPEN_CLOSE_NS.response(201, 'Created.')
    # pylint: disable=R0201
    def post(self):
        """
        Add a new period to the database
        """
        new = OpenClose(**request.get_json())
        DB.session.add(new)
        DB.session.commit()
        return marshal(new, OPEN_CLOSE_GET), 201

@OPEN_CLOSE_NS.route('/<int:period_id>/')
class PeriodDetail(Resource):
    """
    A single period
    """

    @API.marshal_with(OPEN_CLOSE_GET)
    @OPEN_CLOSE_NS.response(404, 'Specified period does not found!')
    # pylint: disable=R0201
    def get(self, period_id):
        """
        Get the details of a single period
        """
        period = OpenClose.query.filter(OpenClose.id == period_id).first()
        if period is None:
            abort(404, 'Specified period does not exist!')
        return period

    @OPEN_CLOSE_NS.doc(model=OPEN_CLOSE_GET, body=OPEN_CLOSE_PUT)
    @OPEN_CLOSE_NS.response(404, 'Specified period not found!')
    # pylint: disable=R0201
    def put(self, period_id):
        """
        Update a single period
        """
        period = OpenClose.query.filter(OpenClose.id == period_id).first()

        if period is None:
            abort(404, 'Specified period not found!')

        period.update(**request.get_json())
        DB.session.commit()
        return marshal(period, OPEN_CLOSE_GET), 200

    @OPEN_CLOSE_NS.response(404, 'Specified period not found!')
    @OPEN_CLOSE_NS.response(204, 'Specified period was deleted!')
    # pylint: disable=R0201
    def delete(self, period_id):
        """
        Drop the period from the DB
        """
        period = OpenClose.query.filter(OpenClose.id == period_id).first()

        if period is None:
            abort(404, 'Specified period not found!')

        DB.session.delete(period)
        DB.session.commit()
        return "", 204




