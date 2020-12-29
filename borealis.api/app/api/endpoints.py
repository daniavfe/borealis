from flask import Blueprint
from flask_restful import Api
from .measurementEndpoint import MeasurementListEndpoint, MeasurementCreationEndpoint
from .stationEndpoint import StationtListEndpoint, StationCreationEndpoint


# Measurement endpoints
measurement_blueprint = Blueprint('measurement_blueprint', __name__)
measurement_api = Api(measurement_blueprint)
measurement_api.add_resource(MeasurementListEndpoint, '/api/measurement/', endpoint='measurement_list_endpoint')
measurement_api.add_resource(MeasurementCreationEndpoint, '/api/measurement/', endpoint='measurement_creation_endpoint')

# Station endpoints
station_blueprint = Blueprint('station_blueprint', __name__)
station_api = Api(station_blueprint)
measurement_api.add_resource(StationtListEndpoint, '/api/station/', endpoint='station_list_endpoint')
measurement_api.add_resource(StationCreationEndpoint, '/api/station/', endpoint='station_creation_endpoint')
