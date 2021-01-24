from flask import request
from flask_restful import  Resource
from ..schema import StationSchema, PFOCollectionSchema
from ..business import stationBusiness

pfocollection_schema = PFOCollectionSchema()

class StationtListEndpoint(Resource):
    @staticmethod
    def get():
        page = request.args.get('page')
        per_page = request.args.get('per_page')
        order_by = request.args.get('order_by')
        order_by_descending = request.args.get('order_by_descending')
        stations = stationBusiness.get_stations(page, per_page, order_by, order_by_descending)
        result = pfocollection_schema.dump(stations, many=False)
        return result

class StationCreationEndpoint(Resource):
    @staticmethod
    def post():
        schema = StationSchema()
        measurement = schema.loads(request.data)
        measurement.save()
