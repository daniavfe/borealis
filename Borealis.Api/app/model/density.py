from ..extension import db
from .base_model import BaseModelMixin


class Density(db.Model, BaseModelMixin):
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'), nullable=False, primary_key=True)
    neighborhood_id = db.Column(db.Integer, db.ForeignKey('neighborhood.id'), nullable=False, primary_key=True)
    date = db.Column(db.DateTime, primary_key=True)
    value = db.Column(db.Integer)


    def __init__(self, district_id, neighborhood_id, date, value):
        self.district_id = district_id
        self.neighborhood_id = neighborhood_id
        self.date = date
        self.value = value

    def __repr__(self):
        return f'Density({self.id})'

    def __str__(self):
        return f'Density({self.id})'

