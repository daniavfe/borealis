from marshmallow import fields, post_load
from app.extension import marshmallow
from ...dto import MeasurementDto
from ..camel_cased_schema import CamelCasedSchema


class MeasurementDtoSchema(CamelCasedSchema):
    town_id = fields.Integer()
    datetime = fields.DateTime()
    magnitude_id = fields.Integer()
    data = fields.Float()
    validation_code = fields.String()
    station_id = fields.String()

    @post_load
    def make(self, data, **kwargs):
        return MeasurementDto(**data)
