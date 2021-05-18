from ..extension import db
from .base_model import BaseModelMixin


class Holiday(db.Model, BaseModelMixin):
    __tablename__ = 'holidays'
    town_id = db.Column(db.Integer, db.ForeignKey("towns.town_id"), primary_key=True)
    date = db.Column(db.DateTime, primary_key=True)
    day_of_week = db.Column(db.Integer)
    name = db.Column(db.String(200))
    scope = db.Column(db.String(50))
    #Navigation properties
    town = db.relationship("Town", back_populates="holidays")

    def __init__(self, date, day_of_week, name, scope):
        self.date = date
        self.day_of_week = day_of_week
        self.name = name
        self.scope = scope

    def __repr__(self):
        return f'Holiday({self.date})'

    def __str__(self):
        return f'Holiday({self.date})'
