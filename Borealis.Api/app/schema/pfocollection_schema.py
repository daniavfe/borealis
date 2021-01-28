from marshmallow import fields, post_load
from app.extension import marshmallow
from ..dto import PFOCollection
from .pollution_measurement_schema import PollutionMeasurementSchema
from .camel_cased_schema import CamelCasedSchema

class PFOCollectionSchema(CamelCasedSchema):
    page = fields.Integer()
    page_count = fields.Integer()
    per_page = fields.Integer()
    order_by = fields.String()
    order_by_descending = fields.Bool()
    items = fields.Nested(PollutionMeasurementSchema, many=True)


    @post_load
    def make_pfo_collection(self, data, **kwargs):
        return PFOCollection(**data)
