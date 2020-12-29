from flask import request, Blueprint
from flask_restful import Api, Resource
from ..schema import MeasurementSchema, PFOCollectionSchema
from ..dto import PFOCollection
from ..business import measurementBusiness


measurement_blueprint = Blueprint('measurement_blueprint', __name__)
pfocollection_schema = PFOCollectionSchema()
api = Api(measurement_blueprint)


class MeasurementListResource(Resource):
    @staticmethod
    def get():
        page = request.args.get('page')
        per_page = request.args.get('per_page')
        order_by = request.args.get('order_by')
        order_by_descending = request.args.get('order_by_descending')

        measurements = measurementBusiness.get_measurements(page, per_page, order_by, order_by_descending)
        result = pfocollection_schema.dump(measurements, many=False)

        return result


class MeasurementCreationResource(Resource):
    @staticmethod
    def post():
        schema = MeasurementSchema()
        measurement = schema.loads(request.data)
        measurement.save()


api.add_resource(MeasurementListResource, '/api/measurement/', endpoint='measurement_list_resource')
api.add_resource(MeasurementCreationResource, '/api/measurement/', endpoint='measurement_creation_resource')
