class StationUpdateDto():
    def __init__(self, name, address, start_date, end_date, latitude, longitude, altitude, neighborhood_id):
        self.name = name
        self.address = address
        self.start_date = start_date
        self.end_date = end_date
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.neighborhood_id = neighborhood_id

