from flask import Blueprint
from flask_restful import Api
from .pollution_endpoint import *
from .density_endpoint import *
from .holiday_endpoint import *


# Measurement endpoints
pollution_blueprint = Blueprint('pollution_blueprint', __name__)
pollution_api = Api(pollution_blueprint)
pollution_api.add_resource(PollutionMeasurementListEndpoint, '/api/pollution/', endpoint='pollution_measurement_list_endpoint')
pollution_api.add_resource(PollutionMeasurementCreationEndpoint, '/api/pollution/', endpoint='pollution_measurement_creation_endpoint')
pollution_api.add_resource(PollutionStationtListEndpoint, '/api/pollution/station/', endpoint='pollution_station_list_endpoint')
pollution_api.add_resource(PollutionStationCreationEndpoint, '/api/pollution/station/', endpoint='pollution_station_creation_endpoint')


# Density endpoints
density_blueprint = Blueprint('density_blueprint', __name__)
density_api = Api(density_blueprint)
density_api.add_resource(DensityDistrictListEndpoint, '/api/density/district/', endpoint='district_list_endpoint')
density_api.add_resource(DensityDistrictCreationEndpoint, '/api/density/district/', endpoint='district_creation_endpoint')
density_api.add_resource(DensityNeighborhoodListEndpoint, '/api/density/neighborhood/', endpoint='neighborhood_list_endpoint')
density_api.add_resource(DensityNeighborhoodCreationEndpoint, '/api/density/neighborhood/', endpoint='neighborhood_creation_endpoint')
density_api.add_resource(DensityListEndpoint, '/api/density/', endpoint='density_list_endpoint')
density_api.add_resource(DensityCreationEndpoint, '/api/density/', endpoint='density_creation_endpoint')


# Holiday endpoints
holiday_blueprint = Blueprint('holiday_blueprint', __name__)
holiday_api = Api(holiday_blueprint)
holiday_api.add_resource(HolidayListEndpoint, '/api/holiday/', endpoint='holiday_list_endpoint')
holiday_api.add_resource(HolidayCreationEndpoint, '/api/holiday/', endpoint='holiday_creation_endpoint')

