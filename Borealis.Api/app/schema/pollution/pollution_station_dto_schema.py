from marshmallow import fields, post_load
from app.extension import marshmallow
from ...dto import PollutionStationDto
from ..camel_cased_schema import CamelCasedSchema

class PollutionStationDtoSchema(CamelCasedSchema):
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
        return PollutionStationDto(**data)
