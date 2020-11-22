from ..extension import db
from .base_model import BaseModelMixin


class Measurement(db.Model, BaseModelMixin):
    province = db.Column(db.Integer, primary_key=True)
    town = db.Column(db.Integer, primary_key=True)
    station = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, primary_key=True)
    magnitude = db.Column(db.Integer)
    method = db.Column(db.Integer)
    analysis_period = db.Column(db.Integer)
    data = db.Column(db.Integer)
    validation_code = db.Column(db.String(1))

    def __init__(self, province, town, station, date, magnitude, method,
                 analysis_period, data, validation_code):
        self.province = province
        self.town = town
        self.station = station
        self.date = date
        self.magnitude = magnitude
        self.method = method
        self.magnitude = magnitude
        self.analysis_period = analysis_period
        self.data = data
        self.validation_code = validation_code

    def __repr__(self):
        return f'Film({self.provice}_{self.town}_{self.station})'

    def __str__(self):
        return f'Film({self.provice}_{self.town}_{self.station})'
