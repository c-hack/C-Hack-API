from time import time
from flask import request
from flask_restplus import Api, Resource, abort, marshal
from sqlalchemy.exc import IntegrityError
from sqlalchemy import and_

from . import API, APP
from .api_models import OPEN_CLOSE_GET, OPEN_CLOSE_POST, OPEN_CLOSE_PUT, OPEN_CLOSE_NOW_GET, OPEN_CLOSE_NOW_INFO_GET

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
    @OPEN_CLOSE_NS.response(400, "Argument Error!")
    # pylint: disable=R0201
    def post(self):
        """
        Add a new period to the database
        """
        new = OpenClose(**request.get_json())
        if new.begin >= new.end:
            abort(400, "begin must be befor end")
        DB.session.add(new)
        DB.session.commit()
        return marshal(new, OPEN_CLOSE_GET), 201


@OPEN_CLOSE_NS.route('/now/')
class NowInPeriod(Resource):
    """
    Return current state
    """

    @API.marshal_with(OPEN_CLOSE_NOW_GET)
    # pylint: disable=R0201
    def get(self):
        now = int(time())
        """
        Get current state
        """
        state = (OpenClose.query.filter(and_(OpenClose.begin < now), (OpenClose.end > now)).count()>0)
        return {'state': state}, 200


@OPEN_CLOSE_NS.route('/now-detailed/')
class NowInPeriodDetailed(Resource):
    """
    Return current state
    """

    @API.marshal_with(OPEN_CLOSE_NOW_INFO_GET)
    # pylint: disable=R0201
    def get(self):
        now = int(time())
        """
        Get current state
        """
        periods = OpenClose.query.filter(and_(OpenClose.begin < now), (OpenClose.end > now)).all()
        return {'state': len(periods)>0, 'current_periods': periods}, 200


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
