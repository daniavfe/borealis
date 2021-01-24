from marshmallow import fields, post_load
from app.extension import marshmallow
from ..model import District
from .camel_cased_schema import CamelCasedSchema


class DistrictSchema(CamelCasedSchema):
    id = fields.String()
    name = fields.String()

    @post_load
    def make_district(self, data, **kwargs):
        return District(**data)



