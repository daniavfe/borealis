from flask import Blueprint
from flask_restful import Api
from .pollution_measurement_endpoint import PollutionMeasurementListEndpoint, PollutionMeasurementCreationEndpoint
from .pollution_station_endpoint import PollutionStationtListEndpoint, PollutionStationCreationEndpoint
from .density_endpoint import *


# Measurement endpoints
measurement_blueprint = Blueprint('pollution_measurement_blueprint', __name__)
measurement_api = Api(measurement_blueprint)
measurement_api.add_resource(PollutionMeasurementListEndpoint, '/api/pollutionMeasurement/', endpoint='pollution_measurement_list_endpoint')
measurement_api.add_resource(PollutionMeasurementCreationEndpoint, '/api/pollutionMeasurement/', endpoint='pollution_measurement_creation_endpoint')

# Station endpoints
station_blueprint = Blueprint('pollution_station_blueprint', __name__)
station_api = Api(station_blueprint)
station_api.add_resource(PollutionStationtListEndpoint, '/api/pollutionStation/', endpoint='pollution_station_list_endpoint')
station_api.add_resource(PollutionStationCreationEndpoint, '/api/pollutionStation/', endpoint='pollution_station_creation_endpoint')


# Density endpoints
density_blueprint = Blueprint('density_blueprint', __name__)
density_api = Api(density_blueprint)
density_api.add_resource(DensityDistrictListEndpoint, '/api/density/district/', endpoint='district_list_endpoint')
density_api.add_resource(DensityDistrictCreationEndpoint, '/api/density/district/', endpoint='district_creation_endpoint')
density_api.add_resource(DensityNeighborhoodListEndpoint, '/api/density/neighborhood/', endpoint='neighborhood_list_endpoint')
density_api.add_resource(DensityNeighborhoodCreationEndpoint, '/api/density/neighborhood/', endpoint='neighborhood_creation_endpoint')
density_api.add_resource(DensityListEndpoint, '/api/density/', endpoint='density_list_endpoint')
density_api.add_resource(DensityCreationEndpoint, '/api/density/', endpoint='density_creation_endpoint')
