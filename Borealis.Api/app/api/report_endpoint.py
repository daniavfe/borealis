from flask import request
from flask_restful import  Resource
from ..schema import *
from ..business import ReportBusiness
from .query_params_helper import QueryParamsHelper
import json

report_business = ReportBusiness()

class ReportCreationEndpoint(Resource):
    @staticmethod
    def get():
        report_dto = report_business.create_report()      
        report_dto_schema = ReportDtoSchema()
        return report_dto_schema.dump(report_dto)

