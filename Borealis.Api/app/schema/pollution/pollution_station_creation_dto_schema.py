from marshmallow import fields, post_load
from app.extension import marshmallow
from ...dto import PollutionStationCreationDto
from ..camel_cased_schema import CamelCasedSchema

class PollutionStationCreationDtoSchema(CamelCasedSchema):
    id = fields.Integer()
    name = fields.String()
    address = fields.String(missing=None)
    start_date = fields.DateTime(missing=None)
    end_date = fields.DateTime(missing=None)
    longitude = fields.String(missing=None)
    latitude = fields.String(missing=None)
    altitude = fields.Integer(missing=None)

    @post_load
    def make(self, data, **kwargs):
        return PollutionStationCreationDto(**data)


