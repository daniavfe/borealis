from ..extension import db
from .base_model import BaseModelMixin


class Timeline(db.Model, BaseModelMixin):
    __tablename__ = 'timelines'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    life_start = db.Column(db.DateTime, nullable=False)
    life_end = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(100))
    details = db.Column(db.String(1000))


    def __init__(self, type, life_start, life_end, status, details):
        self.type = type
        self.life_start = life_start
        self.life_end = life_end
        self.status = status
        self.details = details

    def __repr__(self):
        return f'Timeline({self.timeline_id})'

    def __str__(self):
        return f'Timeline({self.timeline_id})'


