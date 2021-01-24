from flask import request
from flask_restful import  Resource
from ..schema import PollutionMeasurementSchema, PFOCollectionSchema
from ..business import pollutionMeasurementBusiness

pfocollection_schema = PFOCollectionSchema()

class PollutionMeasurementListEndpoint(Resource):
    @staticmethod
    def get():
        page = request.args.get('page')
        per_page = request.args.get('perPage')
        order_by = request.args.get('orderBy')
        order_by_descending = request.args.get('orderByDescending')
        measurements = pollutionMeasurementBusiness.get_measurements(page, per_page, order_by, order_by_descending)
        result = pfocollection_schema.dump(measurements, many=False)
        return result

class PollutionMeasurementCreationEndpoint(Resource):
    @staticmethod
    def post():
        schema = PollutionMeasurementSchema()
        measurement = schema.loads(request.data)
        measurement.save()
