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

class LogEventCreationEndpoint(Resource):
    @staticmethod
    def post():
        #Instance schema
        log_event_creation_dto_schema = LogEventCreationDtoSchema()
        #Parse json to dto
        log_event_creation_dto = log_event_creation_dto_schema.loads(request.data)
        #Create holiday
        event_business.create_log_event(log_event_creation_dto)

class FileDownloadEventCreationEndpoint(Resource):
    @staticmethod
    def post():
        #Instance schema
        file_download_event_creation_dto_schema = FileDownloadEventCreationDtoSchema()
        #Parse json to dto
        file_download_event_creation_dto = file_download_event_creation_dto_schema.loads(request.data)
        #Create holiday
        event_business.create_file_download_event(file_download_event_creation_dto)

class FileUploadEventCreationEndpoint(Resource):
    @staticmethod
    def post():
        #Instance schema
        file_upload_event_creation_dto_schema = FileUploadEventCreationDtoSchema()
        #Parse json to dto
        file_upload_event_creation_dto = file_upload_event_creation_dto_schema.loads(request.data)
        #Create holiday
        event_business.create_file_upload_event(file_upload_event_creation_dto)

