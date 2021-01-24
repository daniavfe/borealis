from flask import Blueprint
from flask_restful import Api
from .pollution_measurement_endpoint import PollutionMeasurementListEndpoint, PollutionMeasurementCreationEndpoint
from .stationEndpoint import StationtListEndpoint, StationCreationEndpoint


# Measurement endpoints
measurement_blueprint = Blueprint('pollution_measurement_blueprint', __name__)
measurement_api = Api(measurement_blueprint)
measurement_api.add_resource(PollutionMeasurementListEndpoint, '/api/pollutionMeasurement/', endpoint='measurement_list_endpoint')
measurement_api.add_resource(PollutionMeasurementCreationEndpoint, '/api/pollutionMeasurement/', endpoint='measurement_creation_endpoint')

# Station endpoints
station_blueprint = Blueprint('station_blueprint', __name__)
station_api = Api(station_blueprint)
measurement_api.add_resource(StationtListEndpoint, '/api/station/', endpoint='station_list_endpoint')
measurement_api.add_resource(StationCreationEndpoint, '/api/station/', endpoint='station_creation_endpoint')
