from marshmallow import fields, post_load
from app.extension import marshmallow
from ...dto import MeasurementBatchCreationResultDto
from ..camel_cased_schema import CamelCasedSchema

class MeasurementBatchCreationResultDtoSchema(CamelCasedSchema):
    items_not_created_positions = fields.List(fields.Integer)

    @post_load
    def make(self, data, **kwargs):
        return MeasurementBatchCreationResultDto(**data)


