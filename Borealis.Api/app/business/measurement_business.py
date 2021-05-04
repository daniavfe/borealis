from ..extension import db
from ..dto import *
from ..model import *
from sqlalchemy import desc, exc
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
        page_count = math.floor(data.count() / per_page);
        page = int(page) if (page != None and int(page) > 0 and int(page) <= page_count) else 1

        data = data.offset(per_page*(page-1)).limit(per_page).all()
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
        
        #items_not_created_positions = []
        #index = 0
        #for measurement_creation_dto in measurement_creation_dto_list:
        #    measurement = Measurement(measurement_creation_dto.town_id,
        #                                    measurement_creation_dto.datetime, 
        #                                    measurement_creation_dto.station_id, 
        #                                    measurement_creation_dto.magnitude_id, 
        #                                    measurement_creation_dto.data, 
        #                                    measurement_creation_dto.validation_code)
        #    try:
        #        measurement.save()
        #    except exc.SQLAlchemyError:
        #        items_not_created_positions.append(index)

        #    index+=1

        #return BatchCreationResultDto(items_not_created_positions)

        data = list(map(lambda x: Measurement(x.town_id,x.datetime, x.station_id, x.magnitude_id, x.data, x.validation_code), measurement_creation_dto_list))

        db.session.add_all(data)
        db.session.commit()
        return BatchCreationResultDto([])

    def assign_station_magnitude(self, station_magnitude_creation_dto):
        # TODO: Comprobaciones
        station_magnitude = PollutionStationMagnitude(station_magnitude_creation_dto.station_id, station_magnitude_creation_dto.magnitude_id)
        station_magnitude.save()
