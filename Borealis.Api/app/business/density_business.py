from ..extension import db
from ..dto import PFOCollection
from ..model import District, Neighborhood, Density
from sqlalchemy import desc
import math

class DensityBusiness:

    def get_districts(self):
        #get data
        return db.session.query(District).all()

    def create_district(self, district):
        #comprobaciones
        district.save()
        return district.id

    def get_neighborhoods(self, district_id):
        return db.session.query(Neighborhood).filter(Neighborhood.district_id == district_id).all();

    def create_neighborhood(self, neightbordhood):
        #comprobaciones
        neightbordhood.save()
        return neightbordhood.id

    def create_density(self, density):
        #comprobaciones
        density.save()
        return 1

