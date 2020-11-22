from flask import request, Blueprint
from flask_restful import Api, Resource
from ..schema import MeasurementSchema
from ..model import Measurement
import datetime


measurement_blueprint = Blueprint('measurement_blueprint', __name__)
measurement_schema = MeasurementSchema()
api = Api(measurement_blueprint)


class MeasurementListResource(Resource):
    @staticmethod
    def get():
        measurements = Measurement.get_all()
        result = measurement_schema.dump(measurements, many=True)
        return result


class MeasurementCreationResource(Resource):
    @staticmethod
    def post():
        measurement = Measurement(0, 0, 0, datetime.datetime(2020, 5, 17), 0, 0, 0, 0, 0)
        measurement.save()
        #return measurement.date


api.add_resource(MeasurementListResource, '/api/measurement/', endpoint='measurement_list_resource')
api.add_resource(MeasurementCreationResource, '/api/measurement/', endpoint='measurement_creation_resource')
