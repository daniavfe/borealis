from marshmallow import fields, post_load
from ...dto import DensityDto
from ..camel_cased_schema import CamelCasedSchema

class DensityDtoSchema(CamelCasedSchema):
    district_id = fields.Integer()
    neighborhood_id = fields.Integer()
    year = fields.Integer()
    month = fields.Integer()
    value = fields.Integer()

    @post_load
    def make(self, data, **kwargs):
        return DensityDto(**data)


