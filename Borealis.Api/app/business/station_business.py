from ..extension import db
from ..dto import *
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

        data = data.offset(per_page*(page-1)).limit(per_page).all()

        mappedData = list(map(lambda x: StationDto(x.id, x.name, x.address, x.start_date, x.end_date, x.latitude, x.longitude, x.altitude), data))
        return PFOCollectionDto(page, page_count, per_page, order_by_field, order_by_descending, mappedData)

    def create_station(self, station_creation_dto):
        #TODO: Comprobaciones
        station = Station(station_creation_dto.id, 
                                             station_creation_dto.name, 
                                             station_creation_dto.address, 
                                             station_creation_dto.start_date,
                                             station_creation_dto.end_date,
                                             station_creation_dto.latitude,
                                             station_creation_dto.longitude,
                                             station_creation_dto.altitude)
        station.save()
        return station.id