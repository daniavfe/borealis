from ..extension import db
from .base_model import BaseModelMixin


class District(db.Model, BaseModelMixin):
    __tablename__ = 'districts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    surface = db.Column(db.Float)
    neighborhoods = db.relationship("Neighborhood")
    densities = db.relationship("Density", backref="district")


    def __init__(self, name, surface):
        self.name = name
        self.surface = surface
 
    def __repr__(self):
        return f'District({self.name})'

    def __str__(self):
        return f'District({self.name})'
