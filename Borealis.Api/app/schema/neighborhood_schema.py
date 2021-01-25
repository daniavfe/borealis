from marshmallow import fields, post_load
from app.extension import marshmallow
from ..model import Neighborhood
from .camel_cased_schema import CamelCasedSchema


class NeighborhoodSchema(CamelCasedSchema):
    id = fields.String()
    district_id = fields.Integer()
    surface = fields.Float()
    name = fields.String()

    @post_load
    def make_neighborhood(self, data, **kwargs):
        return Neighborhood(**data)



