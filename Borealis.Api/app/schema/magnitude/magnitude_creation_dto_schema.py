from marshmallow import fields, post_load
from app.extension import marshmallow
from ...dto import MagnitudeCreationDto
from ..camel_cased_schema import CamelCasedSchema

class MagnitudeCreationDtoSchema(CamelCasedSchema):
    id = fields.Integer()
    name = fields.String(missing=None)
    formula = fields.String(missing=None)
    measurement_unit = fields.String(missing=None)

    @post_load
    def make(self, data, **kwargs):
        return MagnitudeCreationDto(**data)


