from ..extension import db
from .base_model import BaseModelMixin

class Magnitude(db.Model, BaseModelMixin):
    __tablename__ = 'magnitudes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    formula = db.Column(db.String(5))
    measurement_unit = db.Column(db.String(10))
    
    measurements = db.relationship("Measurement", back_populates="magnitude")
    
    def __init__(self, id, name, formula, measurement_unit):
        self.id = id
        self.name = name
        self.formula = formula
        self.measurement_unit = measurement_unit

    def __repr__(self):
        return f'Magnitude({self.id}_{self.name})'

    def __str__(self):
        return f'Magnitude({self.id}_{self.name})'