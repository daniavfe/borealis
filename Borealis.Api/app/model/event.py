from ..extension import db
from .base_model import BaseModelMixin


class Event(db.Model, BaseModelMixin):
    __tablename__ = 'events'
    event_id = db.Column(db.Integer, nullable=False, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    event_type = db.Column(db.String(100), nullable=False)
    details = db.Column(db.String(1000), nullable=True)


    def __init__(self, date, event_type, details):
        self.date = date
        self.event_type = event_type
        self.details = details

    def __repr__(self):
        return f'Event({self.event_id})'

    def __str__(self):
        return f'Event({self.event_id})'


