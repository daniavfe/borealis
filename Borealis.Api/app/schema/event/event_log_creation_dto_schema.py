from marshmallow import fields, post_load
from ...dto import EventLogCreationDto
from ..camel_cased_schema import CamelCasedSchema

class EventLogCreationDtoSchema(CamelCasedSchema):
    message = fields.String()
    
    @post_load
    def make(self, data, **kwargs):
        return EventLogCreationDto(**data)


