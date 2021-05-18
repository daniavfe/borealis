from ..extension import db
from .base_model import BaseModelMixin


class Density(db.Model, BaseModelMixin):
    __tablename__ = 'densities'
    town_id = db.Column(db.Integer, db.ForeignKey("towns.town_id"), primary_key=True)
    district_id = db.Column(db.Integer, db.ForeignKey('districts.id'), nullable=True)
    neighborhood_id = db.Column(db.Integer, db.ForeignKey('neighborhoods.id'), nullable=True)
    year = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)
    #Navigation properties
    town = db.relationship("Town", back_populates="densities")
    district = db.relationship("District", back_populates="densities")
    neighborhood = db.relationship("Neighborhood", back_populates="densities")


    def __init__(self, district_id, neighborhood_id, year, month, value):
        self.district_id = district_id
        self.neighborhood_id = neighborhood_id
        self.year = year
        self.month = month
        self.value = value

    def __repr__(self):
        return f'Density({self.district_id})'

    def __str__(self):
        return f'Density({self.district_id})'

