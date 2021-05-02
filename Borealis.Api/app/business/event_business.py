from ..extension import db
from ..model import Event
from ..dto import *
from sqlalchemy import desc
import math
import datetime

class EventBusiness(object):
    
    def get_events(self, page, per_page, order_by, order_by_descending):       
        order_by_descending = order_by_descending != None and order_by_descending
        order_by_switch = {
            None: Event.date,

        }
        order_by_field = order_by_switch.get(order_by, Event.date)

        #get data
        data = db.session.query(Event)

        #filter data

        #order data
        if(order_by_descending):
            data = data.order_by(desc(order_by_field))
        else:
            data = data.order_by(order_by_field)

        #page data
        per_page = int(per_page) if (per_page != None and int(per_page) > 0) else 10
        page_count = math.floor(data.count() / per_page);
        page = int(page) if (page != None and int(page) > 0 and int(page) <= page_count) else 1

        data = data.offset(per_page*(page-1)).limit(per_page).all()

        mappedData = list(map(lambda x: EventDto(x.event_id, x.date, x.event_type, x.details), data))

        return PFOCollectionDto(page, page_count, per_page, order_by_field, order_by_descending, mappedData)

    def create_log_event(self, event_log_dto):
        self.__create_event__(EventType.Log.name, event_log_dto.message)

    def create_file_download_event(self, file_download_event_dto):
        self.__create_event__(EventType.Download.name, "")

    def create_file_upload_event(self, file_upload_progress_event_dto):
        self.__create_event__(EventType.UploadProgress.name, "")

    def __create_event__(self, event_type, details):
        utc_now = datetime.datetime.utcnow()
        event = Event(utc_now, event_type, details)
        event.save()

