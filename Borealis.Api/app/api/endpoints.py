from flask import Blueprint
from flask_restful import Api
from .measurement_endpoint import *
from .station_endpoint import *
from .magnitude_endpoint import *
from .density_endpoint import *
from .holiday_endpoint import *
from .event_endpoint import *
from .report_endpoint import *
from .timeline_endpoint import *
from .town_endpoint import *


# Measurement endpoints
measurement_blueprint = Blueprint('measurement_blueprint', __name__)
measurement_api = Api(measurement_blueprint)
measurement_api.add_resource(MeasurementListEndpoint, '/api/measurement/', endpoint='measurement_list_endpoint')
measurement_api.add_resource(MeasurementCreationEndpoint, '/api/measurement/', endpoint='measurement_creation_endpoint')
measurement_api.add_resource(MeasurementChartEndpoint, '/api/measurement/chart/', endpoint='measurement_chart_endpoint')
measurement_api.add_resource(MeasurementBatchCreationEndpoint, '/api/measurement/many/', endpoint='measurement_batch_creation_endpoint')

measurement_api.add_resource(PollutionStationMagnitudeEndpoint, '/api/pollution/station/assign/', endpoint='pollution_station_assign_endpoint')

# Station endpoints
station_blueprint = Blueprint('station_blueprint', __name__)
station_api = Api(station_blueprint)
station_api.add_resource(StationListEndpoint, '/api/station/', endpoint='tation_list_endpoint')
station_api.add_resource(StationCreationEndpoint, '/api/station/', endpoint='station_creation_endpoint')
station_api.add_resource(StationUpdateEndpoint, '/api/station/', endpoint='station_update_endpoint')
station_api.add_resource(StationBatchCreationEndpoint, '/api/station/many/', endpoint='station_batch_creation_endpoint')
station_api.add_resource(StationExistenceEndpoint, '/api/station/existence/', endpoint='station_existence_endpoint')

#Magnitude endpoints
magnitude_blueprint = Blueprint('magnitude_blueprint', __name__)
magnitude_api = Api(magnitude_blueprint)
magnitude_api.add_resource(MagnitudeListEndpoint, '/api/magnitude/', endpoint='magnitude_list_endpoint')
magnitude_api.add_resource(MagnitudeCreationEndpoint, '/api/magnitude/', endpoint='magnitude_creation_endpoint')
magnitude_api.add_resource(MagnitudeUpdateEndpoint, '/api/magnitude/', endpoint='magnitude_update_endpoint')
magnitude_api.add_resource(MagnitudeBatchCreationEndpoint, '/api/magnitude/many/', endpoint='magnitude_batch_creation_endpoint')
magnitude_api.add_resource(MagnitudeExistenceEndpoint, '/api/magnitude/existence/', endpoint='magnitude_existence_endpoint')

# Density endpoints
density_blueprint = Blueprint('density_blueprint', __name__)
density_api = Api(density_blueprint)
density_api.add_resource(DensityDistrictListEndpoint, '/api/density/district/', endpoint='district_list_endpoint')
density_api.add_resource(DensityDistrictCreationEndpoint, '/api/density/district/', endpoint='district_creation_endpoint')
density_api.add_resource(DensityNeighborhoodListEndpoint, '/api/density/neighborhood/', endpoint='neighborhood_list_endpoint')
density_api.add_resource(DensityNeighborhoodCreationEndpoint, '/api/density/neighborhood/', endpoint='neighborhood_creation_endpoint')
density_api.add_resource(DensityListEndpoint, '/api/density/', endpoint='density_list_endpoint') 
density_api.add_resource(DensityCreationEndpoint, '/api/density/', endpoint='density_creation_endpoint')
density_api.add_resource(DensityBatchCreationEndpoint, '/api/density/many/', endpoint='density_batch_creation_endpoint')
density_api.add_resource(DensityDataEndpoint, '/api/density/data/', endpoint='density_data_endpoint')

# Holiday endpoints
holiday_blueprint = Blueprint('holiday_blueprint', __name__)
holiday_api = Api(holiday_blueprint)
holiday_api.add_resource(HolidayListEndpoint, '/api/holiday/', endpoint='holiday_list_endpoint')
holiday_api.add_resource(HolidayCreationEndpoint, '/api/holiday/', endpoint='holiday_creation_endpoint')
holiday_api.add_resource(HolidayBatchCreationEndpoint, '/api/holiday/many/', endpoint='holiday_batch_creation_endpoint')
holiday_api.add_resource(HolidayByYearListEndpoint, '/api/holiday/year/', endpoint='holiday_list_by_year_endpoint')

#Town
town_blueprint = Blueprint('town_blueprint', __name__)
town_api = Api(town_blueprint)
town_api.add_resource(TownListEndpoint, '/api/town/', endpoint='town_list_endpoint')
town_api.add_resource(TownCreationEndpoint, '/api/town/', endpoint='town_creation_endpoint')
town_api.add_resource(TownBatchCreationEndpoint, '/api/town/many/', endpoint='town_batch_creation_endpoint')
town_api.add_resource(TownExistenceEndpoint, '/api/town/existence/', endpoint='town_existence_endpoint')

#Event
event_blueprint = Blueprint('event_blueprint', __name__)
event_api = Api(event_blueprint)
event_api.add_resource(EventListEndpoint, '/api/event/', endpoint='event_list_endpoint')
event_api.add_resource(LogEventCreationEndpoint, '/api/event/log/', endpoint='log_event_creation_endpoint')
event_api.add_resource(FileDownloadEventCreationEndpoint, '/api/event/filedownload/', endpoint='file_download_event_creation_endpoint')
event_api.add_resource(FileUploadEventCreationEndpoint, '/api/event/fileupload/', endpoint='file_upload_event_creation_endpoint')

#Report
report_blueprint = Blueprint('report_blueprint', __name__)
report_api = Api(report_blueprint)
report_api.add_resource(ReportCreationEndpoint, '/api/report/', endpoint='report_endpoint')
report_api.add_resource(TownReportCreationEndpoint, '/api/report/town', endpoint='town_report_endpoint')

#Timeline
timeline_blueprint = Blueprint('timeline_blueprint', __name__)
timeline_api = Api(timeline_blueprint)
timeline_api.add_resource(TimelineListEndpoint, '/api/timeline/',endpoint='timeline_list_endpoint')
timeline_api.add_resource(TimelineCreationEndpoint, '/api/timeline/',endpoint='timeline_creation_endpoint')
timeline_api.add_resource(LastTimelineEndpoint, '/api/timeline/last/',endpoint='last_timeline_endpoint')
timeline_api.add_resource(TimelineUpdateEndpoint, '/api/timeline/',endpoint='timeline_update_endpoint')
timeline_api.add_resource(TimelineIntervalEndpoint, '/api/timeline/interval',endpoint='timeline_interval_endpoint')
