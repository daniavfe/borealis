from marshmallow import fields, post_load
from app.extension import marshmallow
from ...dto import TimelineDto
from ..camel_cased_schema import CamelCasedSchema

class TimelineDtoSchema(CamelCasedSchema):
    type= fields.String()
    life_start = fields.DateTime()
    life_end = fields.DateTime()
    status = fields.String()
    details = fields.String()

    @post_load
    def make(self, data, **kwargs):
        return TimelineDto(**data)


