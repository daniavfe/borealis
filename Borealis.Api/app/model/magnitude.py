from ..extension import db
from .base_model import BaseModelMixin

class Magnitude(db.Model, BaseModelMixin):
    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    formula = db.Column(db.String(5), nullable=False)
    measurement_unit = db.Column(db.String(10), nullable=False)
    measurement_technique = db.Column(db.String(100), nullable=False)

    def __init__(self, id, name, formula, measurement_unit, measurement_technique):
        self.id = id
        self.name = name
        self.formula = formula
        self.measurement_unit = measurement_unit
        self.measurement_technique = measurement_technique

    def __repr__(self):
        return f'Station({self.id}_{self.name})'

    def __str__(self):
        return f'Station({self.id}_{self.name})'