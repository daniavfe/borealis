from ..extension import db
from ..dto import *
from ..model import *
from sqlalchemy import desc
import math
import itertools
import datetime

class DensityBusiness:

    def get_districts(self, page, per_page, order_by, order_by_descending):
        order_by_descending = order_by_descending != None and order_by_descending
        order_by_switch = {
            None: District.id,

        }
        order_by_field = order_by_switch.get(order_by, District.id)

        #get data
        data = db.session.query(District)

        #filter data

        #order data
        if(order_by_descending):
            data = data.order_by(desc(order_by_field))
        else:
            data = data.order_by(order_by_field)

        #page data
        per_page = int(per_page) if (per_page != None and int(per_page) > 0) else 10
        page_count = math.floor(data.count() / per_page);
        page = int(page) if (page != None and int(page) > 0 and int(page) <= page_count) else 1

        data = data.offset(per_page*(page-1)).limit(per_page).all()

        mappedData = list(map(lambda x: DistrictDto(x.id, x.name, x.surface), data))
        return PFOCollectionDto(page, page_count, per_page, order_by_field, order_by_descending, mappedData)

    def create_district(self, district_creation_dto):
        # TODO: Comprobaciones
        district = District(district_creation_dto.name, district_creation_dto.surface)
        district.save()
        return district.id

    def get_neighborhoods(self, page, per_page, order_by, order_by_descending, district_id):
        order_by_descending = order_by_descending != None and order_by_descending   
        order_by_switch = {
            None: Neighborhood.id,

        }
        order_by_field = order_by_switch.get(order_by, Neighborhood.id)

        #get data
        data = db.session.query(Neighborhood)

        #filter data
        if district_id != None:
            data = data.filter(Neighborhood.district_id == district_id)

        #order data
        if(order_by_descending):
            data = data.order_by(desc(order_by_field))
        else:
            data = data.order_by(order_by_field)

        #page data
        per_page = int(per_page) if (per_page != None and int(per_page) > 0) else 10
        page_count = math.floor(data.count() / per_page);
        page = int(page) if (page != None and int(page) > 0 and int(page) <= page_count) else 1

        data = data.offset(per_page*(page-1)).limit(per_page).all()

        mappedData = list(map(lambda x: NeighborhoodDto(x.id, x.name, x.surface, x.district_id), data))
        return PFOCollectionDto(page, page_count, per_page, order_by_field, order_by_descending, mappedData)

    def create_neighborhood(self, neighborhood_creation_dto):
         # TODO: Comprobaciones
        neightborhood = Neighborhood(neighborhood_creation_dto.name, neighborhood_creation_dto.surface, neighborhood_creation_dto.district_id)
        neightborhood.save()
        return neightborhood.id

    def get_densities(self, page, per_page, order_by, order_by_descending):
        order_by_descending = order_by_descending != None and order_by_descending
        order_by_switch = {
            None: Density.year
        }
        order_by_field = order_by_switch.get(order_by, Density.year)

        #get data
        data = db.session.query(Density)

        #filter data

        #order data
        if(order_by_descending):
            data = data.order_by(desc(order_by_field))
        else:
            data = data.order_by(order_by_field)

        #page data
        per_page = int(per_page) if (per_page != None and int(per_page) > 0) else 10
        page_count = math.floor(data.count() / per_page);
        page = int(page) if (page != None and int(page) > 0 and int(page) <= page_count) else 1

        data = data.offset(per_page*(page-1)).limit(per_page).all()

        mappedData = list(map(lambda x: DensityDto(x.district_id, x.neighborhood_id, x.year, x.month, x.value), data))
        return PFOCollectionDto(page, page_count, per_page, order_by_field, order_by_descending, mappedData)

    def create_density(self, density_creation_dto):
         # TODO: Comprobaciones
        density = Density(density_creation_dto.district_id, density_creation_dto.neighborhood_id, density_creation_dto.year, density_creation_dto.month, density_creation_dto.value)
        density.save()

    def get_density_data(self, years, districts, neighborhoods, months):

        data = db.session.query(Density).order_by(Density.year.desc(), Density.district_id.desc(), Density.neighborhood_id.desc(), Density.month.desc())
        
        #filters
        if( years != []):
            data = data.filter(Density.year.in_(years))
        if( districts != []):
            data = data.filter(Density.district_id.in_(districts))
        if( neighborhoods != []):
            data = data.filter(Density.neighborhood_id.in_(neighborhoods))
        if( months != []):
            data = data.filter(Density.month.in_(months))
        data = data.all()

        for item in data:
            print(f'{item.district_id}')

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
