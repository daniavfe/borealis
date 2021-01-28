from marshmallow import fields, post_load
from app.extension import marshmallow
from ..model import PollutionMeasurement
from .camel_cased_schema import CamelCasedSchema


class PollutionMeasurementSchema(CamelCasedSchema):
    datetime = fields.DateTime()
    magnitude = fields.Integer()
    method = fields.Integer()
    analysis_period = fields.Integer()
    data = fields.Float()
    validation_code = fields.String()
    station_id = fields.String()

    @post_load
    def make_user(self, data, **kwargs):
        return PollutionMeasurement(**data)
