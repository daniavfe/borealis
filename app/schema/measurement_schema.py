from marshmallow import fields

from app.extension import marshmallow


class MeasurementSchema(marshmallow.Schema):
    province = fields.Integer()
    town = fields.Integer()
    station = fields.Integer()
    date = fields.Date()
    magnitude = fields.Integer()
    method = fields.Integer()
    analysis_period = fields.Integer()
    data = fields.Integer()
    validation_code = fields.Integer()