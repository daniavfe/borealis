class PollutionMeasurementDto(object):
   def __init__(self, datetime, station_id, magnitude_id, data, validation_code):
        self.datetime = datetime
        self.station_id = station_id
        self.magnitude_id = magnitude_id
        self.data = data
        self.validation_code = validation_code


