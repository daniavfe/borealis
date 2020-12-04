from ..extension import db
from .base_model import BaseModelMixin


class Measurement(db.Model, BaseModelMixin):
    province = db.Column(db.Integer, primary_key=True)
    town = db.Column(db.Integer, primary_key=True)
    station = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime, primary_key=True)
    magnitude = db.Column(db.Integer, primary_key=True)
    method = db.Column(db.Integer)
    analysis_period = db.Column(db.Integer)
    data = db.Column(db.Float)
    validation_code = db.Column(db.String(1))

    def __init__(self, province, town, station, datetime, magnitude, method,
                 analysis_period, data, validation_code):
        self.province = province
        self.town = town
        self.station = station
        self.datetime = datetime
        self.magnitude = magnitude
        self.method = method
        self.analysis_period = analysis_period
        self.data = data
        self.validation_code = validation_code

    def __repr__(self):
        return f'Measurement({self.province}_{self.town}_{self.station})'

    def __str__(self):
        return f'measurement({self.province}_{self.town}_{self.station})'
