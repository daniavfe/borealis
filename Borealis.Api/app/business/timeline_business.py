from ..extension import db
from ..dto import *
from ..model import Timeline
from sqlalchemy import desc, exc, func
import math


class TimelineBusiness():
   
    def get_timelines(self, page, per_page, order_by, order_by_descending):
        order_by_descending = order_by_descending != None and order_by_descending
        order_by_switch = {
            None: Timeline.id
        }
        order_by_field = order_by_switch.get(order_by, Timeline.id)

        #get data
        data = db.session.query(Timeline)

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

        mappedData = list(map(lambda x: TimelineDto(x.id, x.type, x.life_start, x.life_end, x.status, x.details), data))
        return PFOCollectionDto(page, page_count, per_page, order_by_field, order_by_descending, mappedData)

    def create_timeline(self, timeline_creation_dto):
        #TODO: Comprobaciones
        timeline = Timeline(timeline_creation_dto.type, 
                            timeline_creation_dto.life_start, 
                            timeline_creation_dto.life_end, 
                            timeline_creation_dto.status, 
                            timeline_creation_dto.details)
        timeline.save()
        return timeline.id

    def update_timeline(self, timeline_id, timeline_update_dto):
        timeline = db.session.query(Timeline).filter(Timeline.id == timeline_id).one()

        if timeline_update_dto.status != None:
            timeline.status = timeline_update_dto.status
        timeline.save()

    def get_last_timeline(self, type = None):
        data = db.session.query(Timeline).filter(Timeline.type == type).order_by(desc(Timeline.life_end)).first()
        if data == None:
            return LastTimelineDto()

        return LastTimelineDto(data.life_end)

    def get_timeline_interval(self, type):
        data = db.session.query(func.min(Timeline.life_start).label('life_start'), func.max(Timeline.life_end).label('life_end')).filter(Timeline.type == type).group_by(Timeline.type).first()
        return TimelineIntervalDto(data.life_start, data.life_end)
