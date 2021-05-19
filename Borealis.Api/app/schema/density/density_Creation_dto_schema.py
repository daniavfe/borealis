from marshmallow import fields, post_load
from ...dto import DensityCreationDto
from ..camel_cased_schema import CamelCasedSchema


class DensityCreationDtoSchema(CamelCasedSchema):
    town_id = fields.Integer()
    district_id = fields.Integer()
    neighborhood_id = fields.Integer()
    year = fields.Integer()
    month = fields.Integer(missing=None)
    value = fields.Integer()

    @post_load
    def make(self, data, **kwargs):
        return DensityCreationDto(**data)
