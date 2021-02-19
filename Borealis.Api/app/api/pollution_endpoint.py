from flask import request
from flask_restful import  Resource
from ..schema import *
from ..business import PollutionBusiness
import json

pollution_business = PollutionBusiness()

class PollutionMeasurementListEndpoint(Resource):
    @staticmethod
    def get():
        page = request.args.get('page')
        per_page = request.args.get('perPage')
        order_by = request.args.get('orderBy')
        order_by_descending = request.args.get('orderByDescending')
        measurements = pollution_business.get_measurements(page, per_page, order_by, order_by_descending)
        pfocollection_schema = PFOCollectionSchema[PollutionMeasurementDtoSchema]()
        result = pfocollection_schema.dump(measurements, many=False)
        return result

class PollutionMeasurementCreationEndpoint(Resource):
    @staticmethod
    def post():
        pollution_measurement_creation_dto_schema = PollutionMeasurementCreationDtoSchema();
        pollution_measurement_creation_dto = pollution_measurement_creation_dto_schema.loads(request.data)
        pollution_business.create_measurement(pollution_measurement_creation_dto)

class PollutionStationtListEndpoint(Resource):
    @staticmethod
    def get():
        page = request.args.get('page')
        per_page = request.args.get('per_page')
        order_by = request.args.get('order_by')
        order_by_descending = request.args.get('order_by_descending')
        stations = pollution_business.get_stations(page, per_page, order_by, order_by_descending)
        pfocollection_schema = PFOCollectionSchema[PollutionStationDtoSchema]()
        result = pfocollection_schema.dump(stations, many=False)
        return result

class PollutionStationCreationEndpoint(Resource):
    @staticmethod
    def post():
        pollution_station_creation_dto_schema = PollutionStationCreationDtoSchema();
        pollution_station_creation_dto = pollution_station_creation_dto_schema.loads(request.data)
        id = pollution_business.create_station(pollution_station_creation_dto)
        return json.dump(id)
