from configuration import HolidayConfiguration
from client import ApiClient
from common import Logger
from measurement import MeasurementParser
from .holiday_downloader import HolidayDownloader
from .holiday_helper import HolidayHelper
from .community_holiday_downloader import CommunityHolidayDownloader
from .community_holiday_helper import CommunityHolidayHelper

import os

class HolidayInitialLoader():
    def __init__(self, holiday_configuration:HolidayConfiguration, api_client:ApiClient, logger:Logger) -> None:
        self.__holiday_configuration__ :HolidayConfiguration = holiday_configuration
        self.__api_client__ :ApiClient = api_client
        self.__logger__ :Logger = logger

    # Realiza la carga inicial de los datos
    def load(self) -> None:
        self.__logger__.info('Holiday initial loader starts');
        holiday_downloader = HolidayDownloader(self.__holiday_configuration__, self.__api_client__, self.__logger__)
        holiday_downloader.download_calendar()
        helper = HolidayHelper(self.__api_client__, self.__logger__)
        measurement_parser = MeasurementParser(self.__api_client__, self.__logger__, helper)
        measurement_parser.upload_all_files(self.__holiday_configuration__.download_path)
        
        community_holiday_downloader = CommunityHolidayDownloader(self.__holiday_configuration__, self.__api_client__, self.__logger__)
        community_holiday_downloader.download_calendar()

        helper = CommunityHolidayHelper(self.__api_client__, self.__logger__)
        measurement_parser = MeasurementParser(self.__api_client__, self.__logger__, helper)
        measurement_parser.upload_all_files(self.__holiday_configuration__.community_download_path)



