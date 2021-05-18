from marshmallow import fields, post_load
from ...dto import TownDto
from ..camel_cased_schema import CamelCasedSchema


class TownDtoSchema(CamelCasedSchema):
    town_id = fields.Integer()
    name = fields.String()

    @post_load
    def make(self, data, **kwargs):
        return TownDto(**data)
