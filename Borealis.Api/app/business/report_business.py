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
    
    def create_report(self):
        all_measurements = db.session.query(Measurement.datetime, Measurement.town_id, Measurement.magnitude_id,Measurement.station_id, Measurement.data, Holiday.name, Holiday.scope).filter(db.extract('year',Measurement.datetime) == 2020).join(Holiday, func.date(Holiday.date) == func.date(Measurement.datetime), isouter=True).order_by(Measurement.datetime, Measurement.town_id).all()
        
        first_measurement = all_measurements[0]
        measurement_list = list()
        current_element = dict()
        current_element['date'] = all_measurements[0].datetime
        current_element['townId'] = all_measurements[0].town_id
        keys = {'date','townId','holidayName','holidayScope'}

        for measurement in all_measurements:
            keys.add(f'{measurement.station_id}{measurement.magnitude_id}')
            if measurement.datetime == current_element['date'] and measurement.town_id == current_element['townId']:
                current_element[f'{measurement.station_id}{measurement.magnitude_id}'] = measurement.data
                current_element['holidayName'] = measurement.name
                current_element['holidayScope'] = measurement.scope
            else:
                measurement_list.append(current_element)
                current_element = dict()
                current_element['date'] = measurement.datetime
                current_element['townId'] = measurement.town_id
                current_element[f'{measurement.station_id}{measurement.magnitude_id}'] = measurement.data
                current_element['holidayName'] = measurement.name
                current_element['holidayScope'] = measurement.scope

        measurement_list.append(current_element)
        
        x = io.StringIO()
        dict_writer = csv.DictWriter(x, keys)
        dict_writer.writeheader()
        dict_writer.writerows(measurement_list)
        encoded = base64.b64encode(x.getvalue().encode('utf-8'))
        return ReportDto(encoded)

