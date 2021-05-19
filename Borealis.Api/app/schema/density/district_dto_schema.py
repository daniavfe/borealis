from marshmallow import fields, post_load
from ...dto import DistrictDto
from ..camel_cased_schema import CamelCasedSchema


class DistrictDtoSchema(CamelCasedSchema):
    id = fields.Integer()
    town_id = fields.Integer()
    name = fields.String()
    surface = fields.Float()
    neighborhood_count = fields.Integer()
    densities_count = fields.Integer()

    @post_load
    def make(self, data, **kwargs):
        return DistrictDto(**data)
