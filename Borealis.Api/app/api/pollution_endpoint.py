from flask import request
from flask_restful import  Resource
from ..schema import *
from ..business import PollutionBusiness
from .query_params_helper import QueryParamsHelper
import json

pollution_business = PollutionBusiness()

class PollutionMeasurementListEndpoint(Resource):
    @staticmethod
    def get():
        #Get params from url
        page, per_page, order_by, order_by_descending = QueryParamsHelper.get_paged_params(request)
        #Get measurements from business
        measurements = pollution_business.get_measurements(page, per_page, order_by, order_by_descending)
        #Instance schema
        pfocollection_schema = get_pfo(PollutionMeasurementDtoSchema)
        #Return json data
        return pfocollection_schema.dump(measurements, many=False)

class PollutionMeasurementCreationEndpoint(Resource):
    @staticmethod
    def post():
        #Instance schema
        pollution_measurement_creation_dto_schema = PollutionMeasurementCreationDtoSchema()
        #Parse json to dto
        pollution_measurement_creation_dto = pollution_measurement_creation_dto_schema.loads(request.data)
        #Create measurement
        pollution_business.create_measurement(pollution_measurement_creation_dto)

class PollutionMeasurementBatchCreationEndpoint(Resource):
    @staticmethod
    def post():
        #Instance schema
        pollution_measurement_creation_dto_schema = PollutionMeasurementCreationDtoSchema()
        #Parse json to dto
        pollution_measurement_creation_dto_list = pollution_measurement_creation_dto_schema.loads(request.data, many=True)
        #Create measurement
        items_not_created = pollution_business.create_measurements_in_batch(pollution_measurement_creation_dto_list)
        #Instance result schema
        pollution_batch_creation_result_dto_schema = PollutionBatchCreationResultDtoSchema()
        #Return json data
        return pollution_batch_creation_result_dto_schema.dump(items_not_created, many=False)

class PollutionStationListEndpoint(Resource):
    @staticmethod
    def get():
        #Get params from url
        page, per_page, order_by, order_by_descending = QueryParamsHelper.get_paged_params(request)
        #Get stations from business
        stations = pollution_business.get_stations(page, per_page, order_by, order_by_descending)
        #Instance schema
        pfocollection_schema = get_pfo(PollutionStationDtoSchema)
        #Return json data
        return pfocollection_schema.dump(stations, many=False)

class PollutionStationCreationEndpoint(Resource):
    @staticmethod
    def post():
        #Instance schema
        pollution_station_creation_dto_schema = PollutionStationCreationDtoSchema()
        #Parse json to dto
        pollution_station_creation_dto = pollution_station_creation_dto_schema.loads(request.data)
        #Create station
        return pollution_business.create_station(pollution_station_creation_dto)

class PollutionStationMagnitudeEndpoint(Resource):
    @staticmethod
    def post():
        #Instance schema
        pollution_station_magnitude_creation_dto_schema = PollutionStationMagnitudeCreationDtoSchema()
        #Parse json to dto
        pollution_station_magnitude_creation_dto = pollution_station_magnitude_creation_dto_schema.loads(request.data)
        #Create station magnitude
        return pollution_business.assign_station_magnitude(pollution_station_magnitude_creation_dto)