from marshmallow import fields, post_load
from app.extension import marshmallow
from ...dto import MagnitudeDto
from ..camel_cased_schema import CamelCasedSchema


class MagnitudeDtoSchema(CamelCasedSchema):
    id = fields.Integer()
    name = fields.String()
    formula = fields.String()
    measurement_unit = fields.String()

    @post_load
    def make(self, data, **kwargs):
        return MagnitudeDto(**data)
