from flask import request
from flask_restful import  Resource
from ..business import MeasurementBusiness
from ..schema import *
from .query_params_helper import QueryParamsHelper
import json

measurement_business = MeasurementBusiness()

class MeasurementListEndpoint(Resource):
    @staticmethod
    def get():
        #Get params from url
        page, per_page, order_by, order_by_descending = QueryParamsHelper.get_paged_params(request)
        #Get measurements from business
        measurements = measurement_business.get_measurements(page, per_page, order_by, order_by_descending)
        #Instance schema
        pfocollection_schema = get_pfo(MeasurementDtoSchema)
        #Return json data
        return pfocollection_schema.dump(measurements, many=False)

class MeasurementCreationEndpoint(Resource):
    @staticmethod
    def post():
        #Instance schema
        measurement_creation_dto_schema = MeasurementCreationDtoSchema()
        #Parse json to dto
        measurement_creation_dto = measurement_creation_dto_schema.loads(request.data)
        #Create measurement
        measurement_business.create_measurement(measurement_creation_dto)

class MeasurementBatchCreationEndpoint(Resource):
    @staticmethod
    def post():
        #Instance schema
        measurement_creation_dto_schema = MeasurementCreationDtoSchema()
        #Parse json to dto
        measurement_creation_dto_list = measurement_creation_dto_schema.loads(request.data, many=True)
        #Create measurement
        items_not_created = measurement_business.create_measurements_in_batch(measurement_creation_dto_list)
        #Instance result schema
        measurement_batch_creation_result_dto_schema = MeasurementBatchCreationResultDtoSchema()
        #Return json data
        return measurement_batch_creation_result_dto_schema.dump(items_not_created, many=False)

class PollutionStationMagnitudeEndpoint(Resource):
    @staticmethod
    def post():
        #Instance schema
        pollution_station_magnitude_creation_dto_schema = PollutionStationMagnitudeCreationDtoSchema()
        #Parse json to dto
        pollution_station_magnitude_creation_dto = pollution_station_magnitude_creation_dto_schema.loads(request.data)
        #Create station magnitude
        return pollution_business.assign_station_magnitude(pollution_station_magnitude_creation_dto)