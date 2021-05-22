from ..extension import db
from ..dto import *
from ..model import *
from sqlalchemy import desc, func
import math
import itertools
import datetime
import base64
import csv
import io

class ReportBusiness():
    
    def create_report(self, year, months, stations, magnitudes):

        # Comprobación de los valores:
        # El año es obgligatorio
        # Si no se especifican meses, se consideran todos
        # Si no se especifican estaciones, se consideran todas
        # Si no se especifican magnitudes, se consideran todas

        if not year:
            raise Exception('Year must be specified')
        
        data = db.session.query(Measurement.datetime, Measurement.town_id, Measurement.magnitude_id,Measurement.station_id, Measurement.data, Holiday.name, Holiday.scope).filter(db.extract('year',Measurement.datetime) == year).join(Holiday, func.date(Holiday.date) == func.date(Measurement.datetime), isouter=True).order_by(Measurement.datetime, Measurement.town_id)
        
        if len(months) > 0:
            data = data.filter(db.extract('month',Measurement.datetime).in_(months))

        if len(stations) > 0:
            data = data.filter(Measurement.station_id.in_(stations))

        if len(magnitudes) > 0:
            data = data.filter(Measurement.magnitude_id.in_(magnitudes))

        all_measurements = data.all()

        
        
        memory_stream = io.StringIO()
        dict_writer = csv.DictWriter(memory_stream, keys)
        dict_writer.writeheader()
        dict_writer.writerows(measurement_list)
        encoded = base64.b64encode(memory_stream.getvalue().encode('utf-8'))
        return ReportDto(encoded)

    def create_town_report(self, year, months, granularity, stations, magnitudes):

        if not year:
            raise Exception('Year must be specified')

        if granularity == 'daily':
            data = db.session.query(db.extract('year', Measurement.datetime), db.extract('month', Measurement.datetime), db.extract('day', Measurement.datetime), Measurement.town_id, Measurement.magnitude_id,Measurement.station_id, func.avg(Measurement.data)).filter(db.extract('year', Measurement.datetime) == year).group_by(db.extract('year', Measurement.datetime), db.extract('month', Measurement.datetime), db.extract('day', Measurement.datetime), Measurement.town_id, Measurement.magnitude_id, Measurement.station_id)
        else:
            data = db.session.query(Measurement.datetime, Measurement.town_id, Measurement.magnitude_id,Measurement.station_id, Measurement.data).filter(db.extract('year', Measurement.datetime) == year)

        #data = data.filter(db.extract('year', Measurement.datetime) == year)

        if len(months) > 0:
            data = data.filter(db.extract('month', Measurement.datetime).in_(months))

        if len(stations) > 0:
            data = data.filter(Measurement.station_id.in_(stations))

        if len(magnitudes) > 0:
            data = data.filter(Measurement.magnitude_id.in_(magnitudes))


        all_measurements = data.all()

        result, keys = self.__get_report_data(all_measurements)

        memory_stream = io.StringIO()
        dict_writer = csv.DictWriter(memory_stream, keys)
        dict_writer.writeheader()
        dict_writer.writerows(result)
        encoded = base64.b64encode(memory_stream.getvalue().encode('utf-8'))
        return ReportDto(encoded)

    def __get_report_data(self, all_measurements):
        first_measurement = all_measurements[0]
        measurement_list = list()
        current_element = dict()
        current_element['date'] = all_measurements[0].datetime
        current_element['townId'] = all_measurements[0].town_id
        keys = {'date','townId','holidayName','holidayScope'}

        for measurement in all_measurements:
            keys.add(f'{measurement.station_id}-{measurement.magnitude_id}')
            if measurement.datetime == current_element['date'] and measurement.town_id == current_element['townId']:
                current_element[f'{measurement.station_id}-{measurement.magnitude_id}'] = measurement.data
                #current_element['holidayName'] = measurement.name
                #current_element['holidayScope'] = measurement.scope
            else:
                measurement_list.append(current_element)
                current_element = dict()
                current_element['date'] = measurement.datetime
                current_element['townId'] = measurement.town_id
                current_element[f'{measurement.station_id}-{measurement.magnitude_id}'] = measurement.data
                #current_element['holidayName'] = measurement.name
                #current_element['holidayScope'] = measurement.scope

        measurement_list.append(current_element)
        return measurement_list, keys