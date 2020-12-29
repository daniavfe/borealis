from ..extension import db
from ..dto import PFOCollection
from ..model import Station
from sqlalchemy import desc
import math

class StationBusiness:

    def get_stations(self, page, per_page, order_by, order_by_descending):
        order_by_descending = order_by_descending != None and order_by_descending
        order_by_switch = {
            None: Station.start_date,
        }
        order_by_field = order_by_switch.get(order_by, Station.start_date)

        #get data
        data = db.session.query(Station)

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

        return PFOCollection(page, page_count, per_page, order_by_field, order_by_descending, data)



stationBusiness = StationBusiness()