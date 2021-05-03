from marshmallow import fields, post_load
from app.extension import marshmallow
from ...dto import StationDto
from ..camel_cased_schema import CamelCasedSchema

class StationDtoSchema(CamelCasedSchema):
    id = fields.Integer()
    name = fields.String()
    address = fields.String()
    start_date = fields.DateTime()
    end_date = fields.DateTime()
    latitude = fields.String()
    longitude = fields.String()
    altitude = fields.Integer()

    @post_load
    def make(self, data, **kwargs):
        return StationDto(**data)
