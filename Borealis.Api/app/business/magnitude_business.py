from ..extension import db
from ..dto import *
from ..model import Magnitude
from sqlalchemy import desc, exc
import math

class MagnitudeBusiness:

    # Obtiene el listado de magnitudes
    def get_magnitudes(self, page, per_page, order_by, order_by_descending):
        order_by_descending = order_by_descending != None and order_by_descending
        order_by_switch = {
            "id": Magnitude.id,
            "name": Magnitude.name,
            None: Magnitude.id
        }
        order_by_field = order_by_switch.get(order_by, Magnitude.id)

        #get data
        data = db.session.query(Magnitude)

        #filter data

        #order data
        if(order_by_descending == True):
            data = data.order_by(desc(order_by_field))
        else:
            data = data.order_by(order_by_field)

        #page data
        per_page = int(per_page) if (per_page != None and int(per_page) > 0) else 10
        page_count = math.floor(data.count() / per_page);
        page = int(page) if (page != None and int(page) > 0 and int(page) <= page_count) else 1

        data = data.offset(per_page*(page-1)).limit(per_page).all()

        mappedData = list(map(lambda x: MagnitudeDto(x.id, x.name, x.formula, x.measurement_unit), data))
        return PFOCollectionDto(page, page_count, per_page, order_by_field, order_by_descending, mappedData)

    def create_magnitude(self, magnitude_creation_dto):
        # TODO: Comprobaciones
        magnitude = Magnitude(magnitude_creation_dto.id,
                                    magnitude_creation_dto.name,
                                    magnitude_creation_dto.formula,
                                    magnitude_creation_dto.measurement_unit)
        magnitude.save()
        return magnitude.id

    def update_magnitude(self, magnitude_id, magnitude_update_dto):
        magnitude = db.session.query(Magnitude).filter(Magnitude.id == magnitude_id).one()

        if magnitude_update_dto.name != None:
            magnitude.name = magnitude_update_dto.name
        if magnitude_update_dto.formula != None:
            magnitude.formula = magnitude_update_dto.formula
        if magnitude_update_dto.measurement_unit != None:
            magnitude.measurement_unit = magnitude_update_dto.measurement_unit

        magnitude.save()

    def create_magnitudes_in_batch(self, magnitude_creation_dto_list):
        items_not_created_positions = []
        index = 0
        for magnitude_creation_dto in magnitude_creation_dto_list:
            magnitude = Magnitude(magnitude_creation_dto.id,
                                    magnitude_creation_dto.name,
                                    magnitude_creation_dto.formula,
                                    magnitude_creation_dto.measurement_unit)
            try:
                magnitude.save()
            except exc.SQLAlchemyError:
                items_not_created_positions.append(index)
            index+=1

        return BatchCreationResultDto(items_not_created_positions)

    # De un listado de ids devuelve aquellas que no existen en base de datos
    def magnitude_existence(self, magnitude_ids):
        db_magnitude_ids = [item.id for item in db.session.query(Magnitude.id).filter(Magnitude.id.in_(magnitude_ids)).all()]
        not_included_magnitudes = list(set([int(item) for item in magnitude_ids]).difference(set(db_magnitude_ids)))
        return ExistenceDto(not_included_magnitudes)


magnitudeBusiness = MagnitudeBusiness()