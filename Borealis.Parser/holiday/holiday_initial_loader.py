from .holiday_downloader import HolidayDownloader
from .holiday_parser import HolidayParser
from configuration import HolidayConfiguration
from client import ApiClient
from common import Logger
import os

class HolidayInitialLoader():
    def __init__(self, holiday_configuration:HolidayConfiguration, api_client:ApiClient, logger:Logger) -> None:
        self.__holiday_configuration__ :HolidayConfiguration = holiday_configuration
        self.__api_client__ :ApiClient = api_client
        self.__logger__ :Logger = logger

    # Realiza la carga inicial de los datos
    def load(self) -> None:
        self.__logger__.info('Holiday initial loader starts');
        holiday_downloader = HolidayDownloader(self.__holiday_configuration__, self.__logger__)
        holiday_downloader.download_calendar()
        holiday_parser = HolidayParser(self.__api_client__, self.__logger__)
        holiday_parser.upload_file(os.path.join(self.__holiday_configuration__.download_path, 'calendar.csv'))


