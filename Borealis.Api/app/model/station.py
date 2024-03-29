from ..extension import db
from .base_model import BaseModelMixin

class Station(db.Model, BaseModelMixin):
    __tablename__ = 'stations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(200))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    latitude = db.Column(db.String(20))
    longitude = db.Column(db.String(20))
    altitude = db.Column(db.Integer)  
    town_id = db.Column(db.Integer, db.ForeignKey('towns.town_id'), nullable=True)
    neighborhood_id = db.Column(db.Integer, db.ForeignKey('neighborhoods.id'), nullable=True)
    #Navigation properties
    town = db.relationship("Town", back_populates="stations")
    neighborhood = db.relationship("Neighborhood", back_populates="stations")
    measurements = db.relationship("Measurement", back_populates="station")
    

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