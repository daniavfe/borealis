from ..extension import db
from ..dto import *
from ..model import *
from datetime import datetime
from sqlalchemy import desc,tuple_, exc, func
import math

class MeasurementBusiness:

    def get_measurements(self, page, per_page, order_by, order_by_descending):
        order_by_descending = order_by_descending != None and order_by_descending
        order_by_switch = {
            None: Measurement.datetime,
            "townId":Measurement.town_id,
            "stationId": Measurement.station_id,
            "datetime":Measurement.datetime,
            "magnitudeId": Measurement.magnitude_id,
            "data": Measurement.data,
            "validationCode":Measurement.validation_code,
        }
        order_by_field = order_by_switch.get(order_by, Measurement.datetime)

        #get data
        data = db.session.query(Measurement)

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
        mappedData = list(map(lambda x: MeasurementDto(x.town_id, x.datetime, x.station_id, x.magnitude_id, x.data, x.validation_code), data))

        return PFOCollectionDto(page, page_count, per_page, order_by_field, order_by_descending, mappedData)

    def create_measurement(self, measurement_creation_dto):
        
        #TODO: Comprobaciones
        measurement = Measurement(measurement_creation_dto.town_id,
                                            measurement_creation_dto.datetime, 
                                            measurement_creation_dto.station_id, 
                                            measurement_creation_dto.magnitude_id, 
                                            measurement_creation_dto.data, 
                                            measurement_creation_dto.validation_code)
        measurement.save()

    def create_measurements_in_batch(self, measurement_creation_dto_list):
       
        data = list(map(lambda x: Measurement(x.town_id,x.datetime, x.station_id, x.magnitude_id, x.data, x.validation_code), measurement_creation_dto_list))

        try:
            db.session.add_all(data)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
            keys = list(map(lambda x: (x.town_id,x.datetime, x.station_id, x.magnitude_id), data))
            existing_items = set(db.session.query(Measurement.town_id, Measurement.datetime,  Measurement.station_id, Measurement.magnitude_id).filter(tuple_(Measurement.town_id, Measurement.datetime,  Measurement.station_id, Measurement.magnitude_id).in_(keys)).all())
            not_existing_items = set(keys).difference(set(existing_items))
            data = [item for item in data if (item.town_id,item.datetime, item.station_id, item.magnitude_id) in not_existing_items]
            db.session.add_all(data)
            db.session.commit()

        return BatchCreationResultDto([])

    def assign_station_magnitude(self, station_magnitude_creation_dto):
        # TODO: Comprobaciones
        station_magnitude = PollutionStationMagnitude(station_magnitude_creation_dto.station_id, station_magnitude_creation_dto.magnitude_id)
        station_magnitude.save()

    def get_measurement_for_charts(self, year, month, granularity, magnitudes):
        
        #if granularity = hourly, month have to be provided
        #if granularity = daily, year have to be provided
        if granularity == 'hourly' and month == None:
            raise Exception('Month must be specified for hourly granularity')

        if granularity == 'daily' and year == None:
            raise Exception('Year must be specified for daily granularity')


        if granularity == 'daily':
            data = db.session.query(db.extract('year', Measurement.datetime).label('year'), db.extract('month', Measurement.datetime).label('month'), db.extract('day', Measurement.datetime).label('day'), Measurement.magnitude_id, func.avg(Measurement.data).label('data')).group_by(db.extract('year', Measurement.datetime),db.extract('month', Measurement.datetime), db.extract('day', Measurement.datetime), Measurement.magnitude_id)
        elif granularity == 'monthly':
            data = data = db.session.query(db.extract('year', Measurement.datetime).label('year'), db.extract('month', Measurement.datetime).label('month'), Measurement.magnitude_id, func.avg(Measurement.data).label('data')).group_by(db.extract('year', Measurement.datetime),db.extract('month', Measurement.datetime), Measurement.magnitude_id)
        else:
            data = data = db.session.query(Measurement.datetime, Measurement.magnitude_id, func.avg(Measurement.data).label('data')).group_by(Measurement.datetime, Measurement.magnitude_id)

        #filter by year
        if year != None:
            data = data.filter(db.extract('year', Measurement.datetime) == year)

        if month != None:
            data = data.filter(db.extract('month', Measurement.datetime) == month)

        #filter by magnitude
        if len(magnitudes) > 0:
            data = data.filter(Measurement.magnitude_id.in_(magnitudes))

        result = data.all()

        return list(map(lambda x: MeasurementDto(0, self.__get_date_from_granularity(x, granularity), 0, x.magnitude_id, x.data, 'V'), result))

    def __get_date_from_granularity(self, item, granularity):
        if granularity == 'daily':
            return datetime(item.year, item.month, item.day)
        elif granularity == 'monthly':
            return datetime(item.year, item.month, 1)
        else:
            return item.datetime