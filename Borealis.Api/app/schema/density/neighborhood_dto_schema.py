from marshmallow import fields, post_load
from ...dto import NeighborhoodDto
from ..camel_cased_schema import CamelCasedSchema

class NeighborhoodDtoSchema(CamelCasedSchema):
    id = fields.Integer()
    name = fields.String()
    surface = fields.Float()
    district_id = fields.Integer()
    densities_count = fields.Integer()

    @post_load
    def make(self, data, **kwargs):
        return NeighborhoodDto(**data)


