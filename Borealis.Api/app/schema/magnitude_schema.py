from marshmallow import fields, post_load
from app.extension import marshmallow
from ..model import PollutionMagnitude


class PollutionMagnitudeSchema(marshmallow.Schema):
    id = fields.Integer()
    name = fields.String()
    formula = fields.String()
    measurement_unit = fields.DateTime()
    measurement_technique = fields.DateTime()

    @post_load
    def make_user(self, data, **kwargs):
        return Magnitude(**data)
