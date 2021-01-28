from ..extension import db
from .base_model import BaseModelMixin

class PollutionStation(db.Model, BaseModelMixin):
    code = db.Column(db.String(20), primary_key=True, )
    address = db.Column(db.String(100))
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime)
    measurements = db.relationship('PollutionMeasurement')

    def __init__(self, code, address, start_date, end_date):
        self.code = code
        self.address = address
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f'Station({self.code}_{self.address})'

    def __str__(self):
        return f'Station({self.code}_{self.address})'