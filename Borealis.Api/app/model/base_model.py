from ..extension import db
from datetime import datetime


class BaseModelMixin:
    creation_date = db.Column(db.DateTime, nullable=True) 

    def save(self):
        self.creation_date = datetime.utcnow()
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_paged(cls):
        return cls.query.limit(10).all()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def simple_filter(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()
