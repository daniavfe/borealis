from marshmallow import fields, post_load
from ...dto import HolidayDto
from ..camel_cased_schema import CamelCasedSchema


class HolidayDtoSchema(CamelCasedSchema):
    town_id = fields.Integer()
    date = fields.DateTime()
    day_of_week = fields.Integer()
    name = fields.String()
    scope = fields.String()

    @post_load
    def make(self, data, **kwargs):
        return HolidayDto(**data)
