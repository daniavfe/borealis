from flask import request
from flask_restful import  Resource
from ..schema import MeasurementSchema, PFOCollectionSchema
from ..business import measurementBusiness

pfocollection_schema = PFOCollectionSchema()

class MeasurementListEndpoint(Resource):
    @staticmethod
    def get():
        page = request.args.get('page')
        per_page = request.args.get('per_page')
        order_by = request.args.get('order_by')
        order_by_descending = request.args.get('order_by_descending')

        measurements = measurementBusiness.get_measurements(page, per_page, order_by, order_by_descending)
        result = pfocollection_schema.dump(measurements, many=False)

        return result

class MeasurementCreationEndpoint(Resource):
    @staticmethod
    def post():
        schema = MeasurementSchema()
        measurement = schema.loads(request.data)
        measurement.save()
