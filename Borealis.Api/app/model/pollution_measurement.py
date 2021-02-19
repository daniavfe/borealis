from ..extension import db
from .base_model import BaseModelMixin


class PollutionMeasurement(db.Model, BaseModelMixin):
    __tablename__ = 'pollution_measurements'
    datetime = db.Column(db.DateTime, primary_key=True)
    magnitude_id = db.Column(db.Integer, db.ForeignKey('pollution_magnitudes.id'), primary_key=True)
    station_id = db.Column(db.Integer, db.ForeignKey("pollution_stations.id"), primary_key=True)
    data = db.Column(db.Float, nullable=False)
    validation_code = db.Column(db.String(1), nullable=False)
    
    
    def __init__(self, datetime, station_id, magnitude_id, data, validation_code):
        self.datetime = datetime
        self.station_id = station_id
        self.magnitude_id = magnitude_id
        self.data = data
        self.validation_code = validation_code

    def __repr__(self):
        return f'Measurement({self.province}_{self.town}_{self.station})'

    def __str__(self):
        return f'measurement({self.province}_{self.town}_{self.station})'
