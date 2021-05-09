from ..extension import db
from .base_model import BaseModelMixin


class Measurement(db.Model, BaseModelMixin):
    __tablename__ = 'measurements'
    town_id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, primary_key=True)
    data = db.Column(db.Float, nullable=False)
    validation_code = db.Column(db.String(1), nullable=False)
    
    station_id = db.Column(db.Integer, db.ForeignKey("stations.id"), primary_key=True)
    station = db.relationship("Station", back_populates="measurements")

    magnitude_id = db.Column(db.Integer, db.ForeignKey('magnitudes.id'), primary_key=True)
    magnitude = db.relationship("Magnitude", back_populates="measurements")

    def __init__(self, town_id, datetime, station_id, magnitude_id, data, validation_code):
        self.town_id = town_id
        self.datetime = datetime
        self.station_id = station_id
        self.magnitude_id = magnitude_id
        self.data = data
        self.validation_code = validation_code

    def __repr__(self):
        return f'Measurement({self.province}_{self.town}_{self.station})'

    def __str__(self):
        return f'Measurement({self.province}_{self.town}_{self.station})'
