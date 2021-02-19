from marshmallow import fields, post_load
from ...model import Holiday
from ..camel_cased_schema import CamelCasedSchema


class HolidayDtoSchema(CamelCasedSchema):
    date = fields.DateTime()
    day_of_week = fields.Integer()
    name = fields.String()
    scope = fields.String()

    @post_load
    def make_holiday(self, data, **kwargs):
        return Holiday(**data)
