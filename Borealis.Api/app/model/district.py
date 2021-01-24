from ..extension import db
from .base_model import BaseModelMixin


class District(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    neighborhoods = db.relationship("Neighborhood")
    densities = db.relationship("Density")


    def __init__(self, name):
        self.name = name
 
    def __repr__(self):
        return f'District({self.name})'

    def __str__(self):
        return f'District({self.name})'
