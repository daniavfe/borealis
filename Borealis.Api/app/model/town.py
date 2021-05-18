from ..extension import db
from .base_model import BaseModelMixin


class Town(db.Model, BaseModelMixin):
    __tablename__ = 'towns'
    town_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    #Navigation properties
    districts = db.relationship("District", back_populates="town")
    densities = db.relationship("Density", back_populates="town")
    holidays = db.relationship("Holiday", back_populates="town")
    measurements = db.relationship("Measurement", back_populates="town")
    stations = db.relationship("Station", back_populates="town")

    def __init__(self, town_id,name):
        self.town_id = town_id
        self.name = name

    def __repr__(self):
        return f'Town({self.town_id})'

    def __str__(self):
        return f'Town({self.town_id})'

