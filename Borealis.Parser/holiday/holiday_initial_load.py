from .holiday_downloader import HolidayDownloader
from .holiday_parser import HolidayParser
from configuration import HolidayConfiguration
from client import ApiClient
import os

class HolidayInitialLoad():
    def __init__(self, holiday_configuration:HolidayConfiguration, api_client:ApiClient) -> None:
        self.__holiday_configuration__ :HolidayConfiguration = holiday_configuration
        self.__api_client__ :ApiClient = api_client

    # Realiza la carga inicial de los datos
    def load(self)->None:
        holiday_downloader = HolidayDownloader(self.__holiday_configuration__)
        holiday_downloader.download_calendar()
        holiday_parser = HolidayParser(self.__api_client__)
        holiday_parser.upload_file(os.path.join(self.__holiday_configuration__.download_path, 'calendar.csv'))


