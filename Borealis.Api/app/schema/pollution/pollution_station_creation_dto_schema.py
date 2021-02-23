from marshmallow import fields, post_load
from app.extension import marshmallow
from ...dto import PollutionStationCreationDto
from ..camel_cased_schema import CamelCasedSchema

class PollutionStationCreationDtoSchema(CamelCasedSchema):
    id = fields.Integer()
    name = fields.String()
    address = fields.String()
    start_date = fields.DateTime()
    end_date = fields.DateTime(missing=None)
    longitude = fields.String()
    latitude = fields.String()
    altitude = fields.Integer()

    @post_load
    def make(self, data, **kwargs):
        return PollutionStationCreationDto(**data)


