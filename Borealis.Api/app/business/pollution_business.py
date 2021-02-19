from ..extension import db
from ..dto import PFOCollection
from ..model import PollutionMeasurement, PollutionStation
from sqlalchemy import desc
import math

class PollutionBusiness:

    def get_measurements(self, page, per_page, order_by, order_by_descending):
        order_by_descending = order_by_descending != None and order_by_descending
        order_by_switch = {
            None: PollutionMeasurement.datetime,
            "province":PollutionMeasurement.province,
            "town": PollutionMeasurement.town,
            "station": PollutionMeasurement.station,
            "datetime":PollutionMeasurement.datetime,
            "magnitude": PollutionMeasurement.magnitude,
            "method": PollutionMeasurement.method,
            "analysisPeriod":PollutionMeasurement.analysis_period,
            "data": PollutionMeasurement.data,
            "validationCode":PollutionMeasurement.validation_code,
        }
        order_by_field = order_by_switch.get(order_by, PollutionMeasurement.datetime)

        #get data
        data = db.session.query(PollutionMeasurement)

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

    def create_measurement(self, pollution_measurement_creation_dto):
        
        #TODO: Comprobaciones
        pollution_measurement = PollutionMeasurement(pollution_measurement_creation_dto.datetime, 
                                                     pollution_measurement_creation_dto.station_id, 
                                                     pollution_measurement_creation_dto.magnitude_id, 
                                                     pollution_measurement_creation_dto.data, 
                                                     pollution_measurement_creation_dto.validation_code)
        pollution_measurement.save()

    def get_stations(self, page, per_page, order_by, order_by_descending):
        order_by_descending = order_by_descending != None and order_by_descending
        order_by_switch = {
            None: PollutionStation.start_date,
        }
        order_by_field = order_by_switch.get(order_by, PollutionStation.start_date)

        #get data
        data = db.session.query(PollutionStation)

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

    def create_station(self, pollution_station_creation_dto):
        
        #TODO: Comprobaciones
        pollution_station = PollutionStation(pollution_station_creation_dto.id, 
                                             pollution_station_creation_dto.name, 
                                             pollution_station_creation_dto.address, 
                                             pollution_station_creation_dto.start_date,
                                             pollution_station_creation_dto.end_date,
                                             pollution_station_creation_dto.latitude,
                                             pollution_station_creation_dto.longitude,
                                             pollution_station_creation_dto.altitude)
        pollution_station.save()
        return pollution_station.Id