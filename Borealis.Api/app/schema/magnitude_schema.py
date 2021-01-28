from marshmallow import fields, post_load
from app.extension import marshmallow
from ..model import Magnitude


class MagnitudeSchema(marshmallow.Schema):
    id = fields.String()
    name = fields.String()
    formula = fields.String()
    measurement_unit = fields.DateTime()
    measurement_technique = fields.DateTime()

    @post_load
    def make_user(self, data, **kwargs):
        return Magnitude(**data)
