from ..extension import db
from .base_model import BaseModelMixin


class Neighborhood(db.Model, BaseModelMixin):
    __tablename__ = 'neighborhoods'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    surface = db.Column(db.Float) 
    district_id = db.Column(db.Integer, db.ForeignKey('districts.id'), nullable=False)
    #Navigation properties
    district = db.relationship("District", back_populates="neighborhoods")
    densities = db.relationship("Density", back_populates="neighborhood")
    stations = db.relationship("Station", back_populates="neighborhood")

    def __init__(self, id, name, surface, district_id):
        self.id = id
        self.name = name
        self.surface = surface
        self.district_id = district_id
 
    def __repr__(self):
        return f'Neighborhood({self.name})'

    def __str__(self):
        return f'Neighborhood({self.name})'
