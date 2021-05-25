from flask import request
from flask_restful import  Resource
from ..business import HolidayBusiness
from .query_params_helper import QueryParamsHelper
from ..schema import *



holiday_business = HolidayBusiness()

class HolidayListEndpoint(Resource):
    @staticmethod
    def get():
        #Get params from url
        page, per_page, order_by, order_by_descending = QueryParamsHelper.get_paged_params(request)
        #Get holidays from business
        holidays = holiday_business.get_holidays(page, per_page, order_by, order_by_descending)
        #Instance schema
        pfocollection_schema = get_pfo(HolidayDtoSchema)
        #Return json data
        return pfocollection_schema.dump(holidays, many=False)

class HolidayCreationEndpoint(Resource):
    @staticmethod
    def post():
        #Instance schema
        holiday_creation_dto_schema = HolidayCreationDtoSchema()
        #Parse json to dto
        holiday_creation_dto = holiday_creation_dto_schema.loads(request.data)
        #Create holiday
        holiday_business.create_holiday(holiday_creation_dto)

class HolidayBatchCreationEndpoint(Resource):
    @staticmethod
    def post():
        #Instance schema
        holiday_creation_dto_schema = HolidayCreationDtoSchema()
        #Parse json to dto
        holiday_creation_dto_list = holiday_creation_dto_schema.loads(request.data, many=True)
        #Create measurement
        items_not_created = holiday_business.create_holidays_in_batch(holiday_creation_dto_list)
        #Instance result schema
        holiday_batch_creation_result_dto_schema = BatchCreationResultDtoSchema()
        #Return json data
        return holiday_batch_creation_result_dto_schema.dump(items_not_created, many=False)

class HolidayByYearListEndpoint(Resource):
    @staticmethod
    def get():
        #Get params from url
        year = QueryParamsHelper.get_param(request, 'year')
        #Get holidays from business
        holidays = holiday_business.get_holidays_by_year(year)
        #Instance schema
        holiday_dto_schema = HolidayDtoSchema()
        #Return json data
        return holiday_dto_schema.dump(holidays, many=True)