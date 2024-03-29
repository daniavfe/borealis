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

class TimelineUpdateEndpoint(Resource):
    @staticmethod
    def put():
        #Get params from url
        timeline_id = request.args.get('timelineId')
        #Instance schema
        timeline_update_dto_schema = TimelineUpdateDtoSchema()
        #Parse json to dto
        timeline_update_dto = timeline_update_dto_schema.loads(request.data)
        #Create station
        return timeline_business.update_timeline(timeline_id, timeline_update_dto)

class LastTimelineEndpoint(Resource):
    @staticmethod
    def get():
        #Get params from url
        type = request.args.get('type')
        #Get timelines from business
        timeline = timeline_business.get_last_timeline(type)
        #Instance schema
        last_timeline_dto_schema = LastTimelineDtoSchema()
        #Return json data
        return last_timeline_dto_schema.dump(timeline)

class TimelineIntervalEndpoint(Resource):
    @staticmethod
    def get():
        #Get params from url
        type = request.args.get('type')
        #Get timeline interval from business
        timeline_interval = timeline_business.get_timeline_interval(type)
        #Instance schema
        timeline_interval_dto_schema = TimelineIntervalDtoSchema()
        #Return json data
        return timeline_interval_dto_schema.dump(timeline_interval)