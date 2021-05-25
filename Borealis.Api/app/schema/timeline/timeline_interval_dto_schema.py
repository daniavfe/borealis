from marshmallow import fields, post_load
from app.extension import marshmallow
from ...dto import TimelineIntervalDto
from ..camel_cased_schema import CamelCasedSchema

class TimelineIntervalDtoSchema(CamelCasedSchema):
    life_start = fields.DateTime()
    life_end = fields.DateTime()

    @post_load
    def make(self, data, **kwargs):
        return TimelineIntervalDto(**data)


