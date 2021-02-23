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
