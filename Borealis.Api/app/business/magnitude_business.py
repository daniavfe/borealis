from ..extension import db
from ..dto import *
from ..model import PollutionMagnitude
from sqlalchemy import desc
import math

class MagnitudeBusiness:

    def get_magnitudes(self, page, per_page, order_by, order_by_descending):
        order_by_descending = order_by_descending != None and order_by_descending
        order_by_switch = {
            None: Magnitude.id,
        }
        order_by_field = order_by_switch.get(order_by, Magnitude.id)

        #get data
        data = db.session.query(Magnitude)

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

        data = data.offset(per_page*page-1).limit(per_page).all()

        return PFOCollectionDto(page, page_count, per_page, order_by_field, order_by_descending, data)



magnitudeBusiness = MagnitudeBusiness()