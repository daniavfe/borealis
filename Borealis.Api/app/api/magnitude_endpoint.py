from flask import request
from flask_restful import  Resource
from ..schema import *
from ..business import MagnitudeBusiness
from .query_params_helper import QueryParamsHelper
import json

magnitude_business = MagnitudeBusiness()

class MagnitudeListEndpoint(Resource):
    @staticmethod
    def get():
        #Get params from url
        page, per_page, order_by, order_by_descending = QueryParamsHelper.get_paged_params(request)
        #Get stations from business
        magnitudes = magnitude_business.get_magnitudes(page, per_page, order_by, order_by_descending)
        #Instance schema
        pfocollection_schema = get_pfo(MagnitudeDtoSchema)
        #Return json data
        return pfocollection_schema.dump(magnitudes, many=False)

class MagnitudeCreationEndpoint(Resource):
    @staticmethod
    def post():
        #Instance schema
        magnitude_creation_dto_schema = MagnitudeCreationDtoSchema()
        #Parse json to dto
        magnitude_creation_dto = magnitude_creation_dto_schema.loads(request.data)
        #Create magnitude
        return magnitude_business.create_magnitude(magnitude_creation_dto)

class MagnitudeUpdateEndpoint(Resource):
    @staticmethod
    def put():
        #Get params from url
        magnitude_id = request.args.get('id')
        #Instance schema
        magnitude_update_dto_schema = MagnitudeUpdateDtoSchema()
        #Parse json to dto
        magnitude_update_dto = magnitude_update_dto_schema.loads(request.data)
        #Create station
        return magnitude_business.update_magnitude(magnitude_id, magnitude_update_dto)

class MagnitudeBatchCreationEndpoint(Resource):
    @staticmethod
    def post():
        #Instance schema
        magnitude_creation_dto_schema = MagnitudeCreationDtoSchema()
        #Parse json to dto
        magnitude_creation_dto_list = magnitude_creation_dto_schema.loads(request.data, many=True)
        #Create measurement
        items_not_created = magnitude_business.create_magnitudes_in_batch(magnitude_creation_dto_list)
        #Instance result schema
        magnitude_batch_creation_result_dto_schema = BatchCreationResultDtoSchema()
        #Return json data
        return magnitude_batch_creation_result_dto_schema.dump(items_not_created, many=False)

class MagnitudeExistenceEndpoint(Resource):
    @staticmethod
    def get():
        #Get params from url
        magnitude_ids = request.args.getlist('ids')
        #Get not found magnitude ids
        magnitude_existence_dto = magnitude_business.magnitude_existence(magnitude_ids)
        #Instance schema
        magnitude_existence_dto_schema = ExistenceDtoSchema()
        #Return json data
        return magnitude_existence_dto_schema.dump(magnitude_existence_dto, many=False)

