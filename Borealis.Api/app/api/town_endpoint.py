from flask import request
from flask_restful import  Resource
from .query_params_helper import QueryParamsHelper
from ..business import TownBusiness
from ..schema import *

town_business = TownBusiness()

class TownListEndpoint(Resource):
    @staticmethod
    def get():
        #Get params from url
        page, per_page, order_by, order_by_descending = QueryParamsHelper.get_paged_params(request)
        #Get holtownsidays from business
        towns = town_business.get_towns(page, per_page, order_by, order_by_descending)
        #Instance schema
        pfocollection_schema = get_pfo(TownDtoSchema)
        #Return json data
        return pfocollection_schema.dump(towns, many=False)

class TownCreationEndpoint(Resource):
    @staticmethod
    def post():
        #Instance schema
        town_creation_dto_schema = TownCreationDtoSchema()
        #Parse json to dto
        town_creation_dto = town_creation_dto_schema.loads(request.data)
        #Create town
        town_business.create_town(town_creation_dto)

class TownBatchCreationEndpoint(Resource):
    @staticmethod
    def post():
        #Instance schema
        town_creation_dto_schema = TownCreationDtoSchema()
        #Parse json to dto
        town_creation_dto_list = town_creation_dto_schema.loads(request.data, many=True)
        #Create town
        items_not_created = town_business.create_towns_in_batch(town_creation_dto_list)
        #Instance result schema
        town_batch_creation_result_dto_schema = BatchCreationResultDtoSchema()
        #Return json data
        return town_batch_creation_result_dto_schema.dump(items_not_created, many=False)

class TownExistenceEndpoint(Resource):
    @staticmethod
    def get():
        #Get params from url
        town_ids = request.args.getlist('ids')
        #Get not found magnitude ids
        town_existence_dto = town_business.town_existence(town_ids)
        #Instance schema
        town_existence_dto_schema = ExistenceDtoSchema()
        #Return json data
        return town_existence_dto_schema.dump(town_existence_dto, many=False)

