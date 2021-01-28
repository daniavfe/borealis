from marshmallow import fields, post_load
from app.extension import marshmallow
from ..model import Density
from .camel_cased_schema import CamelCasedSchema


class DensitySchema(CamelCasedSchema):
    district_id = fields.Integer()
    neighborhood_id = fields.Integer()
    year = fields.Integer()
    month = fields.Integer()
    value = fields.Integer()

    @post_load
    def make_density(self, data, **kwargs):
        return Density(**data)



