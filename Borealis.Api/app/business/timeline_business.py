from ..extension import db
from ..dto import *
from ..model import Timeline
from sqlalchemy import desc, exc
import math


class TimelineBusiness():
   
    def get_timelines(self, page, per_page, order_by, order_by_descending):
        order_by_descending = order_by_descending != None and order_by_descending
        order_by_switch = {
            None: Timeline.creation_date
        }
        order_by_field = order_by_switch.get(order_by, Timeline.creation_date)

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

