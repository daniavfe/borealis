from marshmallow import fields, post_load
from app.extension import marshmallow
from ..dto import BatchCreationResultDto
from .camel_cased_schema import CamelCasedSchema

class BatchCreationResultDtoSchema(CamelCasedSchema):
    items_not_created_positions = fields.List(fields.Integer)

    @post_load
    def make(self, data, **kwargs):
        return BatchCreationResultDto(**data)


