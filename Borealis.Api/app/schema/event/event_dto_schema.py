from marshmallow import fields, post_load
from ...dto import EventDto
from ..camel_cased_schema import CamelCasedSchema


class EventDtoSchema(CamelCasedSchema):
    event_id = fields.Integer()
    date = fields.DateTime()
    event_type = fields.String()
    details = fields.String()

    @post_load
    def make(self, data, **kwargs):
        return EventDto(**data)



