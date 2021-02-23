from marshmallow import fields, post_load
from app.extension import marshmallow
from ...dto import PollutionMagnitudeCreationDto
from ..camel_cased_schema import CamelCasedSchema

class PollutionMagnitudeCreationDtoSchema(CamelCasedSchema):
    id = fields.Integer()
    name = fields.String()
    formula = fields.String()
    measurement_unit = fields.String()

    @post_load
    def make(self, data, **kwargs):
        return PollutionMagnitudeCreationDto(**data)


