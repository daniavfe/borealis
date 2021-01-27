from flask import request
from flask_restful import  Resource
import json
from ..business import DensityBusiness
from ..schema import *

district_schema = DistrictSchema();
neighborhood_schema = NeighborhoodSchema();
density_schema = DensitySchema();
density_business = DensityBusiness()
densityDataDtoSchema = DensityDataDtoSchema()

class DensityDistrictListEndpoint(Resource):
    @staticmethod
    def get():
        districts = density_business.get_districts()
        result = district_schema.dump(districts, many=True)
        return result

class DensityDistrictCreationEndpoint(Resource):
    @staticmethod
    def post():
        district = district_schema.loads(request.data)
        return density_business.create_district(district)

class DensityNeighborhoodListEndpoint(Resource):
    @staticmethod
    def get():
        district = request.args.get('district_id')
        neightbordhoods = density_business.get_neighborhoods(district)
        result = neighborhood_schema.dump(neightbordhoods, many=True)
        return result;

class DensityNeighborhoodCreationEndpoint(Resource):
    @staticmethod
    def post():
        neighborhood = neighborhood_schema.loads(request.data)
        return density_business.create_neighborhood(neighborhood)

class DensityListEndpoint(Resource):
    @staticmethod
    def get():
        years = request.args.getlist('years')
        districts = request.args.getlist('districts')
        neighborhoods = request.args.getlist('neighborhoods')
        months = request.args.getlist('months')

        densities = density_business.get_densities(years, districts, neighborhoods, months)
        return densityDataDtoSchema.dump(densities, many=True)

class DensityCreationEndpoint(Resource):
    @staticmethod
    def post():
        density = density_schema.loads(request.data)
        return density_business.create_density(density)
