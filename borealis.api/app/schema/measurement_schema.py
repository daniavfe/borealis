from marshmallow import fields, post_load
from app.extension import marshmallow
from ..model import Measurement


class MeasurementSchema(marshmallow.Schema):
    province = fields.Integer()
    town = fields.Integer()
    station = fields.Integer()
    datetime = fields.DateTime()
    magnitude = fields.Integer()
    method = fields.Integer()
    analysis_period = fields.Integer()
    data = fields.Float()
    validation_code = fields.String()

    @post_load
    def make_user(self, data, **kwargs):
        return Measurement(**data)
