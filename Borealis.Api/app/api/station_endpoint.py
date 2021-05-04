from flask import request
from flask_restful import  Resource
from ..schema import *
from ..business import StationBusiness
from .query_params_helper import QueryParamsHelper
import json

station_business = StationBusiness()

class StationListEndpoint(Resource):
    @staticmethod
    def get():
        #Get params from url
        page, per_page, order_by, order_by_descending = QueryParamsHelper.get_paged_params(request)
        #Get stations from business
        stations = station_business.get_stations(page, per_page, order_by, order_by_descending)
        #Instance schema
        pfocollection_schema = get_pfo(StationDtoSchema)
        #Return json data
        return pfocollection_schema.dump(stations, many=False)

class StationCreationEndpoint(Resource):
    @staticmethod
    def post():
        #Instance schema
        station_creation_dto_schema = StationCreationDtoSchema()
        #Parse json to dto
        station_creation_dto = station_creation_dto_schema.loads(request.data)
        #Create station
        return station_business.create_station(station_creation_dto)

class StationBatchCreationEndpoint(Resource):
    @staticmethod
    def post():
        #Instance schema
        station_creation_dto_schema = StationCreationDtoSchema()
        #Parse json to dto
        station_creation_dto_list = station_creation_dto_schema.loads(request.data, many=True)
        #Create measurement
        items_not_created = station_business.create_stations_in_batch(station_creation_dto_list)
        #Instance result schema
        batch_creation_result_dto_schema = BatchCreationResultDtoSchema()
        #Return json data
        return batch_creation_result_dto_schema.dump(items_not_created, many=False)