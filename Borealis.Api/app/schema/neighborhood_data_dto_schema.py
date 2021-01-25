from marshmallow import fields, post_load
from app.extension import marshmallow
from ..dto import NeighborhoodDataDto
from .camel_cased_schema import CamelCasedSchema


class NeighborhoodDataDtoSchema(CamelCasedSchema):
    id = fields.Number()
    name = fields.String()
    values = fields.Dict()

    @post_load
    def make_neighborhood_data_dto(self, data, **kwargs):
        return NeighborhoodDataDto(**data)
