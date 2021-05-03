from marshmallow import fields, post_load
from ...dto import LogEventCreationDto
from ..camel_cased_schema import CamelCasedSchema

class LogEventCreationDtoSchema(CamelCasedSchema):
    message = fields.String()
    
    @post_load
    def make(self, data, **kwargs):
        return LogEventCreationDto(**data)


