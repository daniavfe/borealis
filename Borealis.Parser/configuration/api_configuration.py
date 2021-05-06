class ApiConfiguration():
    def __init__(self, 
        base_url:str, 
        district_endpoint:str, 
        neighborhood_endpoint:str, 
        density_endpoint:str, 
        holiday_endpoint:str, 
        measurement_endpoint:str, 
        station_endpoint:str, 
        magnitude_endpoint:str,
        event_endpoint:str) -> None:

        self.base_url :str = base_url 
        self.district_endpoint :str = district_endpoint
        self.neighborhood_endpoint :str = neighborhood_endpoint
        self.density_endpoint :str = density_endpoint
        self.holiday_endpoint :str = holiday_endpoint
        self.measurement_endpoint :str = measurement_endpoint
        self.station_endpoint :str = station_endpoint
        self.magnitude_endpoint :str = magnitude_endpoint
        self.event_endpoint :str = event_endpoint


