from marshmallow import fields, post_load
from app.extension import marshmallow
from ...dto import LastTimelineDto
from ..camel_cased_schema import CamelCasedSchema

class LastTimelineDtoSchema(CamelCasedSchema):
    life_end = fields.DateTime(missing=None)
    
    @post_load
    def make(self, data, **kwargs):
        return LastTimelineDto(**data)


