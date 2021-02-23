from marshmallow import fields, post_load
from app.extension import marshmallow
from ..dto import PFOCollectionDto
from .camel_cased_schema import CamelCasedSchema
from typing import TypeVar, Generic, List, Tuple


def get_pfo(schema):
    class PFOCollectionDtoSchema(CamelCasedSchema):
            page = fields.Integer()
            page_count = fields.Integer()
            per_page = fields.Integer()
            order_by = fields.String()
            order_by_descending = fields.Bool() 
            items = fields.Nested(schema, many=True);

            @post_load
            def make(self, data, **kwargs):
                return PFOCollectionDto(**data)

    return PFOCollectionDtoSchema()

