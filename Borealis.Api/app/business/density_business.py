from ..extension import db
from ..dto import PFOCollection, DensityDataDto, DistrictDataDto, NeighborhoodDataDto
from ..model import District, Neighborhood, Density
from sqlalchemy import desc
import math
import itertools
import datetime

class DensityBusiness:

    def get_districts(self):
        #get data
        return db.session.query(District).all()

    def create_district(self, district):
        #comprobaciones
        district.save()
        return district.id

    def get_neighborhoods(self, district_id):
        return db.session.query(Neighborhood).filter(Neighborhood.district_id == district_id).all()

    def create_neighborhood(self, neightbordhood):
        #comprobaciones
        neightbordhood.save()
        return neightbordhood.id

    def create_density(self, density):
        #comprobaciones
        density.save()
        return 1

    def get_densities(self):

        data = db.session.query(Density).order_by(Density.year.desc(), Density.district_id.desc(), Density.neighborhood_id.desc(), Density.month.desc()).all()
        
        year_key_func = lambda x: x.year
        district_key_func = lambda x: x.district_id
        neighborhood_key_func = lambda x: x.neighborhood_id
        
        year_list = []          
        for year, year_group in itertools.groupby(data, year_key_func):
            district_list = []
            for district, district_group in itertools.groupby(year_group, district_key_func):
                districts = list(district_group)
                district_name = districts[0].district.name;
                neighborhood_list = []
                for neighborhood, neighborhood_group in itertools.groupby(districts, neighborhood_key_func):
                    neighborhoods = list(neighborhood_group)
                    neighborhood_name = neighborhoods[0].neighborhood.name
                    values = list(map(lambda x:(x.month, x.value), neighborhoods))
                    neighborhood_list.append(NeighborhoodDataDto(neighborhood, neighborhood_name, values))

                district_list.append(DistrictDataDto(district, district_name, neighborhood_list))

            year_list.append(DensityDataDto(year, district_list))

        return year_list
