from marshmallow import fields, post_load
from app.extension import marshmallow
from ..dto import DensityDataDto
from .camel_cased_schema import CamelCasedSchema
from .district_data_dto_schema import DistrictDataDtoSchema

class DensityDataDtoSchema(CamelCasedSchema):
    year = fields.Integer()
    districts = fields.Nested(DistrictDataDtoSchema, many=True)

    @post_load
    def make_density_data_dto(self, data, **kwargs):
        return DensityDataDto(**data)
