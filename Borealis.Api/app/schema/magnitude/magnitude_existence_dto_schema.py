from marshmallow import fields, post_load
from ...dto import MagnitudeExistenceDto
from ..camel_cased_schema import CamelCasedSchema

class MagnitudeExistenceDtoSchema(CamelCasedSchema):
    magnitude_ids = fields.List(fields.Integer)

    @post_load
    def make(self, data, **kwargs):
        return MagnitudeExistenceDto(**data)


