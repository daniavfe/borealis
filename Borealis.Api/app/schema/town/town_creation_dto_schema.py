from marshmallow import fields, post_load
from ...dto import TownCreationDto
from ..camel_cased_schema import CamelCasedSchema


class TownCreationDtoSchema(CamelCasedSchema):
    town_id = fields.Integer()
    name = fields.String(missing=None)

    @post_load
    def make(self, data, **kwargs):
        return TownCreationDto(**data)
