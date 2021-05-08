from marshmallow import fields, post_load
from app.extension import marshmallow
from ...dto import TimelineUpdateDto
from ..camel_cased_schema import CamelCasedSchema

class TimelineUpdateDtoSchema(CamelCasedSchema):
    status = fields.String(missing=None)
    details = fields.String(missing=None)
    

    @post_load
    def make(self, data, **kwargs):
        return TimelineUpdateDto(**data)


