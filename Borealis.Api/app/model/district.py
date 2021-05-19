from ..extension import db
from .base_model import BaseModelMixin


class District(db.Model, BaseModelMixin):
    __tablename__ = 'districts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    surface = db.Column(db.Float)
    town_id = db.Column(db.Integer, db.ForeignKey('towns.town_id'), nullable=False)
    #Navigation properties
    town = db.relationship("Town", back_populates="districts")
    neighborhoods = db.relationship("Neighborhood", back_populates="district")
    densities = db.relationship("Density", back_populates="district")


    def __init__(self, id, town_id, name, surface):
        self.id = id
        self.town_id = town_id
        self.name = name
        self.surface = surface
 
    def __repr__(self):
        return f'District({self.name})'

    def __str__(self):
        return f'District({self.name})'
