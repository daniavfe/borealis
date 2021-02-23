from marshmallow import fields, post_load
from app.extension import marshmallow
from ...dto import PollutionMagnitudeDto
from ..camel_cased_schema import CamelCasedSchema


class PollutionMagnitudeDtoSchema(CamelCasedSchema):
    id = fields.Integer()
    name = fields.String()
    formula = fields.String()
    measurement_unit = fields.String()

    @post_load
    def make(self, data, **kwargs):
        return PollutionMagnitudeDto(**data)
