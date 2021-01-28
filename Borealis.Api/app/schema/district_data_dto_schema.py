from marshmallow import fields, post_load
from app.extension import marshmallow
from ..dto import DistrictDataDto
from .camel_cased_schema import CamelCasedSchema
from .neighborhood_data_dto_schema import NeighborhoodDataDtoSchema


class DistrictDataDtoSchema(CamelCasedSchema):
    id = fields.Integer()
    name = fields.String()
    neighborhoods= fields.Nested(NeighborhoodDataDtoSchema, many=True)

    @post_load
    def make_district_data_dto(self, data, **kwargs):
        return DistrictDataDto(**data)
