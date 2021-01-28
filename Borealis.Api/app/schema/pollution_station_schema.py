from marshmallow import fields, post_load
from app.extension import marshmallow
from ..model import PollutionStation
from .camel_cased_schema import CamelCasedSchema


class PollutionStationSchema(CamelCasedSchema):
    code = fields.String()
    address = fields.String()
    start_date = fields.DateTime()
    end_date = fields.DateTime()

    @post_load
    def make_user(self, data, **kwargs):
        return PollutionStation(**data)
