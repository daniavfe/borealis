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
        #Get url params
        year = request.args.get('year')
        months = request.args.getlist('months')
        station_ids = request.args.getlist('stationIds')
        magnitude_ids = request.args.getlist('magnitudeIds')
        #get report from business
        report_dto = report_business.create_report(year, months, station_ids, magnitude_ids)      
        #Instance schema
        report_dto_schema = ReportDtoSchema()
        #Return json data
        return report_dto_schema.dump(report_dto)

class TownReportCreationEndpoint(Resource):
    @staticmethod
    def get():
        #Get url params
        year = request.args.get('year')
        months = request.args.getlist('months')
        station_ids = request.args.getlist('stationIds')
        granularity = request.args.get('granularity')
        magnitude_ids = request.args.getlist('magnitudeIds')
        towns = request.args.getlist('towns')
        #get report from business
        report_dto = report_business.create_town_report(year,granularity,towns, months, station_ids, magnitude_ids)      
        #Instance schema
        report_dto_schema = ReportDtoSchema()
        #Return json data
        return report_dto_schema.dump(report_dto)

