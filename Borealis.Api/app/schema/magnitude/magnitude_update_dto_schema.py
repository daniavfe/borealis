from marshmallow import fields, post_load
from app.extension import marshmallow
from ...dto import MagnitudeUpdateDto
from ..camel_cased_schema import CamelCasedSchema

class MagnitudeUpdateDtoSchema(CamelCasedSchema):
    name = fields.String(missing=None)
    formula = fields.String(missing=None)
    measurement_unit = fields.String(missing=None)

    @post_load
    def make(self, data, **kwargs):
        return MagnitudeUpdateDto(**data)


