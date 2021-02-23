from marshmallow import fields, post_load
from ...dto import DistrictDto
from ..camel_cased_schema import CamelCasedSchema


class DistrictDtoSchema(CamelCasedSchema):

    @post_load
    def make(self, data, **kwargs):
        return DistrictDto(**data)
