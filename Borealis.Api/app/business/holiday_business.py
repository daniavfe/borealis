from ..extension import db
from ..model import Holiday
from ..dto import *
from sqlalchemy import desc, tuple_, exc
import math
from datetime import datetime

class HolidayBusiness:

    def get_holidays(self, page, per_page, order_by, order_by_descending):
        order_by_descending = order_by_descending != None and order_by_descending
        order_by_switch = {
            None: Holiday.date,

        }
        order_by_field = order_by_switch.get(order_by, Holiday.date)

        #get data
        data = db.session.query(Holiday)

        #filter data

        #order data
        if(order_by_descending):
            data = data.order_by(desc(order_by_field))
        else:
            data = data.order_by(order_by_field)

        #page data
        per_page = int(per_page) if (per_page != None and int(per_page) > 0) else 10
        page_count = math.floor(data.count() / per_page)
        page = int(page) if (page != None and int(page) > 0 and int(page) <= page_count) else 1

        data = data.offset(per_page * (page - 1)).limit(per_page).all()

        mappedData = list(map(lambda x: HolidayDto(x.date, x.day_of_week, x.name, x.scope), data))
        return PFOCollectionDto(page, page_count, per_page, order_by_field, order_by_descending, mappedData)

    def create_holiday(self, holiday_creation_dto):
        # TODO: Comprobaciones
        holiday = Holiday(holiday_creation_dto.town_id, holiday_creation_dto.date, holiday_creation_dto.day_of_week, holiday_creation_dto.name,holiday_creation_dto.scope)
        holiday.save()

    def create_holidays_in_batch(self, holiday_creation_dto_list):
        data = list(map(lambda x: Holiday(x.town_id, x.date, x.day_of_week,x.name, x.scope), holiday_creation_dto_list))

        try:
            db.session.add_all(data)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
            keys = list(map(lambda x: (x.town_id, x.date), data))
            existing_items = set(db.session.query(Holiday.town_id, Holiday.date).filter(tuple_(Holiday.town_id, Holiday.date).in_(keys)).all())
            not_existing_items = set(keys).difference(set(existing_items))
            data = [item for item in data if (item.town_id, item.date) in not_existing_items]
            db.session.add_all(data)
            db.session.commit()

            
        return BatchCreationResultDto([])

