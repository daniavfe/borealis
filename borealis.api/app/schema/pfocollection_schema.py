from marshmallow import fields, post_load
from app.extension import marshmallow
from ..dto import PFOCollection
from .measurement_schema import MeasurementSchema


class PFOCollectionSchema(marshmallow.Schema):
    page = fields.Integer()
    page_count = fields.Integer()
    per_page = fields.Integer()
    order_by = fields.String()
    order_by_descending = fields.Bool()
    items = fields.Nested(MeasurementSchema, many=True)


    @post_load
    def make_pfo_collection(self, data, **kwargs):
        return PFOCollection(**data)