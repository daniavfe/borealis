from marshmallow import fields, post_load
from app.extension import marshmallow
from ...dto import PollutionMeasurementDto
from ..camel_cased_schema import CamelCasedSchema


class PollutionMeasurementDtoSchema(CamelCasedSchema):
    datetime = fields.DateTime()
    magnitude_id = fields.Integer()
    data = fields.Float()
    validation_code = fields.String()
    station_id = fields.String()

    @post_load
    def make(self, data, **kwargs):
        return PollutionMeasurementDto(**data)
