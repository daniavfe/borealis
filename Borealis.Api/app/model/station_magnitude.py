from ..extension import db
from .base_model import BaseModelMixin

class StationMagnitude(db.Model, BaseModelMixin):
    __tablename__ = 'stations_magnitudes'
    station_id = db.Column(db.Integer, db.ForeignKey('stations.id'), primary_key=True)
    magnitude_id = db.Column(db.Integer, db.ForeignKey('magnitudes.id'), primary_key=True)

    station = db.relationship("Station", backref="magnitudes")
    magnitude = db.relationship("Magnitude", backref="stations")

    def __init__(self, station_id, magnitude_id):
        self.station_id = station_id
        self.magnitude_id = magnitude_id

    def __repr__(self):
        return f'StationMagnitudes({self.station_id})'

    def __str__(self):
        return f'StationMagnitudes({self.station_id})'