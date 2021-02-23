from marshmallow import fields, post_load
from app.extension import marshmallow
from ...dto import PollutionMagnitudeCreationDto

class PollutionMagnitudeCreationDtoSchema(marshmallow.Schema):
    id = fields.Integer()
    name = fields.String()
    formula = fields.String()
    measurement_unit = fields.DateTime()
    measurement_technique = fields.DateTime()

    @post_load
    def make(self, data, **kwargs):
        return PollutionMagnitudeCreationDto(**data)


