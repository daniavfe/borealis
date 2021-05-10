from marshmallow import fields, post_load
from app.extension import marshmallow
from ...dto import NeighborhoodCreationDto
from ..camel_cased_schema import CamelCasedSchema


class NeighborhoodCreationDtoSchema(CamelCasedSchema):
    id = fields.Integer()
    district_id = fields.Integer()
    surface = fields.Float()
    name = fields.String()

    @post_load
    def make(self, data, **kwargs):
        return NeighborhoodCreationDto(**data)



