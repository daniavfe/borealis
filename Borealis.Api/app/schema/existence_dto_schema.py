from marshmallow import fields, post_load
from ..dto import ExistenceDto
from .camel_cased_schema import CamelCasedSchema

class ExistenceDtoSchema(CamelCasedSchema):
    ids = fields.List(fields.Integer)

    @post_load
    def make(self, data, **kwargs):
        return ExistenceDto(**data)


