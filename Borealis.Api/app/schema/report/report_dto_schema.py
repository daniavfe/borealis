from marshmallow import fields, post_load
from app.extension import marshmallow
from ...dto import ReportDto
from ..camel_cased_schema import CamelCasedSchema

class ReportDtoSchema(CamelCasedSchema):
    file = fields.String()

    @post_load
    def make(self, data, **kwargs):
        return ReportDto(**data)


