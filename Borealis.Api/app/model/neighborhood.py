from ..extension import db
from .base_model import BaseModelMixin


class Neighborhood(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'), nullable=False)
    densities = db.relationship("Density", backref="neighborhood")


    def __init__(self, name, district_id):
        self.name = name
        self.district_id = district_id
 

    def __repr__(self):
        return f'Neighborhood({self.name})'

    def __str__(self):
        return f'Neighborhood({self.name})'
