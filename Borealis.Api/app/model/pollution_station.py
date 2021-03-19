from ..extension import db
from .base_model import BaseModelMixin

class PollutionStation(db.Model, BaseModelMixin):
    __tablename__ = 'pollution_stations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(200), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime)
    latitude = db.Column(db.String(20))
    longitude = db.Column(db.String(20))
    altitude = db.Column(db.Integer)
    
    measurements = db.relationship("PollutionMeasurement", backref="station")
    #magnitudes = db.relationship('PollutionStationMagnitude', back_populates="stations")
    
    def __init__(self, id, name, address, start_date, end_date, latitude, longitude, altitude):
        self.id = id
        self.name = name
        self.address = address
        self.start_date = start_date
        self.end_date = end_date
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude

    def __repr__(self):
        return f'Station({self.code}_{self.address})'

    def __str__(self):
        return f'Station({self.code}_{self.address})'