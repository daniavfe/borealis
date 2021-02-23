from marshmallow import fields, post_load
from app.extension import marshmallow
from ...dto import PollutionStationMagnitudeCreationDto
from ..camel_cased_schema import CamelCasedSchema

class PollutionStationMagnitudeCreationDtoSchema(CamelCasedSchema):
    station_id = fields.Integer()
    magnitude_id = fields.Integer()

    @post_load
    def make(self, data, **kwargs):
        return PollutionStationMagnitudeCreationDto(**data)


