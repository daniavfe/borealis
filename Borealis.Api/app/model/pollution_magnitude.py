from ..extension import db
from .base_model import BaseModelMixin

class PollutionMagnitude(db.Model, BaseModelMixin):
    __tablename__ = 'pollution_magnitudes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    formula = db.Column(db.String(5), nullable=False)
    measurement_unit = db.Column(db.String(10), nullable=False)
    
    measurements = db.relationship("PollutionMeasurement", backref="magnitude")
    #stations = db.relationship('PollutionStationMagnitude',  back_populates="magnitudes")

    def __init__(self, id, name, formula, measurement_unit):
        self.id = id
        self.name = name
        self.formula = formula
        self.measurement_unit = measurement_unit

    def __repr__(self):
        return f'Station({self.id}_{self.name})'

    def __str__(self):
        return f'Station({self.id}_{self.name})'