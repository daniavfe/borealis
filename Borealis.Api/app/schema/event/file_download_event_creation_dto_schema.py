from marshmallow import fields, post_load
from ...dto import FileDownloadEventCreationDto
from ..camel_cased_schema import CamelCasedSchema

class FileDownloadEventCreationDtoSchema(CamelCasedSchema):
    file_name = fields.String()
    file_size = fields.Float()
    
    @post_load
    def make(self, data, **kwargs):
        return FileDownloadEventCreationDto(**data)


