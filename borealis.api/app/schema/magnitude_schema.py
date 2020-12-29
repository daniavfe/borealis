from marshmallow import fields, post_load
from app.extension import marshmallow
from ..model import Station


class StationSchema(marshmallow.Schema):
    code = fields.String()
    address = fields.String()
    start_date = fields.DateTime()
    end_date = fields.DateTime()

    @post_load
    def make_user(self, data, **kwargs):
        return Station(**data)
