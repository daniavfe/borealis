from flask import request
from flask_restful import  Resource
from ..business import HolidayBusiness
from ..schema import *

holiday_schema = HolidaySchema();
holiday_business = HolidayBusiness()

class HolidayListEndpoint(Resource):
    @staticmethod
    def get():
        holidays = holiday_business.get_holidays()
        result = holiday_schema.dump(holidays, many=True)
        return result

class HolidayCreationEndpoint(Resource):
    @staticmethod
    def post():
        holiday = holiday_schema.loads(request.data)
        return holiday_business.create_holiday(holiday)


