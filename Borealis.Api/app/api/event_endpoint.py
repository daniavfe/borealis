from flask import request
from flask_restful import  Resource
from ..business import EventBusiness
from .query_params_helper import QueryParamsHelper
from ..schema import *

event_business = EventBusiness()

class EventListEndpoint(Resource):
    @staticmethod
    def get():
        #Get params from url
        page, per_page, order_by, order_by_descending = QueryParamsHelper.get_paged_params(request)
        #Get holidays from business
        events = event_business.get_events(page, per_page, order_by, order_by_descending)
        #Instance schema
        pfocollection_schema = get_pfo(EventDtoSchema)
        #Return json data
        return pfocollection_schema.dump(events, many=False)

class EventLogCreationEndpoint(Resource):
    @staticmethod
    def post():
        #Instance schema
        event_log_creation_dto_schema = EventLogCreationDtoSchema()
        #Parse json to dto
        event_log_creation_dto = event_log_creation_dto_schema.loads(request.data)
        #Create holiday
        event_business.create_log_event(event_log_creation_dto)

