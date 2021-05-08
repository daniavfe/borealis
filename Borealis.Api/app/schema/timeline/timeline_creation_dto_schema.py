from marshmallow import fields, post_load
from app.extension import marshmallow
from ...dto import TimelineCreationDto
from ..camel_cased_schema import CamelCasedSchema

class TimelineCreationDtoSchema(CamelCasedSchema):
    type = fields.String()
    life_start = fields.DateTime()
    life_end = fields.DateTime()
    status = fields.String(missing=None)
    details = fields.String(missing=None)
    

    @post_load
    def make(self, data, **kwargs):
        return TimelineCreationDto(**data)


