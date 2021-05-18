from ..extension import db
from ..model import Town
from ..dto import *
from sqlalchemy import desc
import math

class TownBusiness:

    def get_towns(self, page, per_page, order_by, order_by_descending):
        order_by_descending = order_by_descending != None and order_by_descending
        order_by_switch = {
            None: Town.creation_date,

        }
        order_by_field = order_by_switch.get(order_by, Town.creation_date)

        #get data
        data = db.session.query(Town)

        #filter data

        #order data
        if(order_by_descending):
            data = data.order_by(desc(order_by_field))
        else:
            data = data.order_by(order_by_field)

        #page data
        per_page = int(per_page) if (per_page != None and int(per_page) > 0) else 10
        page_count = math.floor(data.count() / per_page)
        page = int(page) if (page != None and int(page) > 0 and int(page) <= page_count) else 1

        data = data.offset(per_page * (page - 1)).limit(per_page).all()

        mappedData = list(map(lambda x: TownDto(x.town_id, x.name), data))
        return PFOCollectionDto(page, page_count, per_page, order_by_field, order_by_descending, mappedData)

    def create_town(self, town_creation_dto):
        # TODO: Comprobaciones
        town = Town(town_creation_dto.town_id, town_creation_dto.name)
        town.save()

    def create_towns_in_batch(self, town_creation_dto_list):
        data = list(map(lambda x: Town(x.town_id, x.name), town_creation_dto_list))
        db.session.add_all(data)
        db.session.commit()
        return BatchCreationResultDto([])
    
    def town_existence(self, town_ids):
        db_town_ids = [item.town_id for item in db.session.query(Town.town_id).filter(Town.town_id.in_(town_ids)).all()]
        not_included_towns = list(set([int(item) for item in town_ids]).difference(set(db_town_ids)))
        return ExistenceDto(not_included_towns)