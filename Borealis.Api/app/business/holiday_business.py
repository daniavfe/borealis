from ..extension import db
from ..model import Holiday
from sqlalchemy import desc

class HolidayBusiness:

    def get_holidays(self):
        #get data
        return db.session.query(Holiday).all()

    def create_holiday(self, holiday):
        #comprobaciones
        holiday.save()
        return holiday.day_of_week
