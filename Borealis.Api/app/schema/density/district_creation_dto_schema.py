from marshmallow import fields, post_load
from app.extension import marshmallow
from ...dto import DistrictCreationDto
from ..camel_cased_schema import CamelCasedSchema


class DistrictCreationDtoSchema(CamelCasedSchema):
    name = fields.String()
    surface = fields.Float()

    @post_load
    def make(self, data, **kwargs):
        return DistrictCreationDto(**data)



