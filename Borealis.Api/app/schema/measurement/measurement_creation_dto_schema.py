from marshmallow import fields, post_load
from app.extension import marshmallow
from ...dto import MeasurementCreationDto
from ..camel_cased_schema import CamelCasedSchema

class MeasurementCreationDtoSchema(CamelCasedSchema):
    town_id = fields.Integer(missing=None)
    datetime = fields.DateTime(missing=None)
    magnitude_id = fields.Integer(missing=None)
    station_id = fields.Integer(missing=None)
    data = fields.Float(missing=None)
    validation_code = fields.String(missing=None)

    @post_load
    def make(self, data, **kwargs):
        return MeasurementCreationDto(**data)