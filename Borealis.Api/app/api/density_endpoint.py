from flask import request
from flask_restful import  Resource
from ..schema import *
from ..business import DensityBusiness
from .query_params_helper import QueryParamsHelper
import json

density_business = DensityBusiness()

class DensityDistrictListEndpoint(Resource):
    @staticmethod
    def get():
        #Get params from url
        page, per_page, order_by, order_by_descending = QueryParamsHelper.get_paged_params(request)
        #Get districts from business
        districts = density_business.get_districts(page, per_page, order_by, order_by_descending)
        #Instance schema
        pfocollection_schema = PFOCollectionDtoSchema[DistrictDtoSchema]()
        #Return json data
        return pfocollection_schema.dump(districts, many=False)

class DensityDistrictCreationEndpoint(Resource):
    @staticmethod
    def post():
        #Instance schema
        district_creation_dto_schema = DistrictCreationDtoSchema()
        #Parse json to dto
        district_creation_dto = district_creation_dto_schema.loads(request.data)
        #Create district
        density_business.create_district(district_creation_dto)

class DensityNeighborhoodListEndpoint(Resource):
    @staticmethod
    def get():
        #Get params from url
        page, per_page, order_by, order_by_descending = QueryParamsHelper.get_paged_params(request)
        district_id = request.args.get('district_id')
        #Get neighborhoods from business
        neightborhoods = density_business.get_neighborhoods(page, per_page, order_by, order_by_descending, district_id)
        #Instance schema
        pfocollection_schema = PFOCollectionDtoSchema[NeighborhoodDtoSchema]()
        #Return json data
        return pfocollection_schema.dump(districts, many=False)

class DensityNeighborhoodCreationEndpoint(Resource):
    @staticmethod
    def post():
        #Instance schema
        neighborhood_creation_dto_schema = NeighborhoodCreationDtoSchema()
        #Parse json to dto
        neighborhood_creation_dto = neighborhood_creation_dto_schema.loads(request.data)
        #Create neighborhood
        density_business.create_neighborhood(neighborhood_creation_dto)

class DensityListEndpoint(Resource):
    @staticmethod
    def get():
        #Get params from url
        page, per_page, order_by, order_by_descending = QueryParamsHelper.get_paged_params(request)
        district_id = request.args.get('district_id')
        neighborhood_id = request.args.get('neighborhood_id')
        #Get districts from business
        densitites = density_business.get_densities(page, per_page, order_by, order_by_descending, district_id, neighborhood_id)
        #Instance schema
        pfocollection_schema = PFOCollectionDtoSchema[DensityDtoSchema]()
        #Return json data
        return pfocollection_schema.dump(densitites, many=False)

class DensityCreationEndpoint(Resource):
    @staticmethod
    def post():
        #Instance schema
        density_creation_dto_schema = DensityCreationDtoSchema()
        #Parse json to dto
        density_creation_dto = density_creation_dto_schema.loads(request.data)
        #Create density
        return density_business.create_density(density_creation_dto)

class DensityDataEndpoint(Resource):
    @staticmethod
    def get():
        #Get params from url
        years = request.args.getlist('years')
        districts = request.args.getlist('districts')
        neighborhoods = request.args.getlist('neighborhoods')
        months = request.args.getlist('months')
        #Get density data from business
        densities = density_business.get_density_data(years, districts, neighborhoods, months)
        #Instance schema
        density_data_dto_schema = DensityDataDtoSchema()
        #Return json data
        return density_data_dto_schema.dump(densities, many=True)