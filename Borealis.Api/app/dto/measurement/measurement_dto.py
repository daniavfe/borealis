class MeasurementDto(object):
   def __init__(self, town_id, datetime, station_id, magnitude_id, data, validation_code):
        self.town_id = town_id
        self.datetime = datetime
        self.station_id = station_id
        self.magnitude_id = magnitude_id
        self.data = data
        self.validation_code = validation_code


