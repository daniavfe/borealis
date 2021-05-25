from ..extension import db
from ..dto import *
from ..model import *
from sqlalchemy import desc, func
import math
import itertools
from datetime import datetime
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

        result, keys = self.__get_hourly_report_data(all_measurements)
        
        memory_stream = io.StringIO()
        dict_writer = csv.DictWriter(memory_stream, keys)
        dict_writer.writeheader()
        dict_writer.writerows(measurement_list)
        encoded = base64.b64encode(memory_stream.getvalue().encode('utf-8'))
        return ReportDto(encoded)

    def create_town_report(self, year,granularity, towns, months, stations, magnitudes):

        if not year:
            raise Exception('Year must be specified')

        if granularity == 'daily':
            data = db.session.query(db.extract('year', Measurement.datetime).label("year"), db.extract('month', Measurement.datetime).label("month"), db.extract('day', Measurement.datetime).label("day"), Measurement.town_id, Measurement.magnitude_id,Measurement.station_id, func.avg(Measurement.data).label("data")) \
                             .group_by(db.extract('year', Measurement.datetime), db.extract('month', Measurement.datetime), db.extract('day', Measurement.datetime), Measurement.town_id, Measurement.magnitude_id, Measurement.station_id)
        elif granularity == 'monthly':
             data = db.session.query(db.extract('year', Measurement.datetime).label("year"), db.extract('month', Measurement.datetime).label("month"), Measurement.town_id, Measurement.magnitude_id,Measurement.station_id, func.avg(Measurement.data).label("data")) \
                             .group_by(db.extract('year', Measurement.datetime), db.extract('month', Measurement.datetime), Measurement.town_id, Measurement.magnitude_id, Measurement.station_id)
        else:
            data = db.session.query(Measurement.datetime, Measurement.town_id, Measurement.magnitude_id,Measurement.station_id, Measurement.data)

        data = data.filter(db.extract('year', Measurement.datetime) == year)

        if len(months) > 0:
            data = data.filter(db.extract('month', Measurement.datetime).in_(months))

        if len(towns) > 0:
            data = data.filter(Measurement.town_id.in_(towns))

        if len(stations) > 0:
            data = data.filter(Measurement.station_id.in_(stations))

        if len(magnitudes) > 0:
            data = data.filter(Measurement.magnitude_id.in_(magnitudes))


        all_measurements = data.all()

        
        if granularity == 'daily':
            result, keys = self.__get_daily_report_data(all_measurements)
        elif granularity == 'monthly':
            result, keys = self.__get_monthly_report_data(all_measurements)
        else:
            result, keys = self.__get_hourly_report_data(all_measurements)

        memory_stream = io.StringIO()
        dict_writer = csv.DictWriter(memory_stream, keys)
        dict_writer.writeheader()
        dict_writer.writerows(result)
        encoded = base64.b64encode(memory_stream.getvalue().encode('utf-8'))
        return ReportDto(encoded)

    def __get_monthly_report_data(self, all_measurements):     
        measurement_list = list()
        current_element = dict()
        keys = {'date','townId','holidayName','holidayScope'}
        
        if len(all_measurements)==0:
            return measurement_list, keys

        first_measurement = all_measurements[0]
        current_element['date'] = datetime(all_measurements[0].year, all_measurements[0].month,1)
        current_element['townId'] = all_measurements[0].town_id
        

        for measurement in all_measurements:
            keys.add(f'{measurement.station_id}-{measurement.magnitude_id}')
            date = datetime(measurement.year, measurement.month,1)
            town_id = measurement.town_id
            data = measurement.data

            if date == current_element['date'] and town_id == current_element['townId']:
                current_element[f'{measurement.station_id}-{measurement.magnitude_id}'] = data
                #current_element['holidayName'] = measurement.name
                #current_element['holidayScope'] = measurement.scope
            else:
                measurement_list.append(current_element)
                current_element = dict()
                current_element['date'] = date
                current_element['townId'] = town_id
                current_element[f'{measurement.station_id}-{measurement.magnitude_id}'] = data
                #current_element['holidayName'] = measurement.name
                #current_element['holidayScope'] = measurement.scope

        measurement_list.append(current_element)
        return measurement_list, keys

    def __get_daily_report_data(self, all_measurements):        
        measurement_list = list()
        current_element = dict()
        keys = {'date','townId','holidayName','holidayScope'}

        if len(all_measurements)==0:
            return measurement_list, keys

        first_measurement = all_measurements[0]
        current_element['date'] = datetime(all_measurements[0].year, all_measurements[0].month, all_measurements[0].day)
        current_element['townId'] = all_measurements[0].town_id
        

        for measurement in all_measurements:
            keys.add(f'{measurement.station_id}-{measurement.magnitude_id}')
            date = datetime(measurement.year, measurement.month, measurement.day)
            town_id = measurement.town_id
            data = measurement.data

            if date == current_element['date'] and town_id == current_element['townId']:
                current_element[f'{measurement.station_id}-{measurement.magnitude_id}'] = data
                #current_element['holidayName'] = measurement.name
                #current_element['holidayScope'] = measurement.scope
            else:
                measurement_list.append(current_element)
                current_element = dict()
                current_element['date'] = date
                current_element['townId'] = town_id
                current_element[f'{measurement.station_id}-{measurement.magnitude_id}'] = data
                #current_element['holidayName'] = measurement.name
                #current_element['holidayScope'] = measurement.scope

        measurement_list.append(current_element)
        return measurement_list, keys

    def __get_hourly_report_data(self, all_measurements):
        measurement_list = list()
        current_element = dict()
        keys = {'date','townId','holidayName','holidayScope'}

        if len(all_measurements)==0:
            return measurement_list, keys

        first_measurement = all_measurements[0]
        
        current_element['date'] = all_measurements[0].datetime
        current_element['townId'] = all_measurements[0].town_id
        

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