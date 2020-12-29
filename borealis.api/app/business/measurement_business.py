from ..extension import db
from ..model import Measurement

class MeasurementBusiness:

    def getMeasurements(self):



        return db.session.query(Measurement).limit(10).offset(10).all()


measurementBusiness = MeasurementBusiness()