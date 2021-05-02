from marshmallow import fields, post_load
from ...dto import FileUploadEventCreationDto
from ..camel_cased_schema import CamelCasedSchema

class FileUploadEventCreationDtoSchema(CamelCasedSchema):
    file_id = fields.Integer()
    file_name = fields.String()
    upload_progress = fields.Float()
    
    @post_load
    def make(self, data, **kwargs):
        return FileUploadEventCreationDto(**data)


