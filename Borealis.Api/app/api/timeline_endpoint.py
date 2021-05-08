from flask import request
from flask_restful import  Resource
from ..business import TimelineBusiness
from .query_params_helper import QueryParamsHelper
from ..schema import *

timeline_business = TimelineBusiness()

class TimelineListEndpoint(Resource):
    @staticmethod
    def get():
        #Get params from url
        page, per_page, order_by, order_by_descending = QueryParamsHelper.get_paged_params(request)
        #Get holidays from business
        timelines = timeline_business.get_timelines(page, per_page, order_by, order_by_descending)
        #Instance schema
        pfocollection_schema = get_pfo(TimelineDtoSchema)
        #Return json data
        return pfocollection_schema.dump(timelines, many=False)

class TimelineCreationEndpoint(Resource):
    @staticmethod
    def post():
        #Instance schema
        timeline_creation_dto_schema = TimelineCreationDtoSchema()
        #Parse json to dto
        timeline_creation_dto = timeline_creation_dto_schema.loads(request.data)
        #Create station
        return timeline_business.create_timeline(timeline_creation_dto)

