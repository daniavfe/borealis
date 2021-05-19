from measurement import MeasurementParser
from configuration import MeteorologyConfiguration
from client import ApiClient
from common import Logger
from .meteorology_helper import MeteorologyHelper
from .meteorology_downloader import MeteorologyDownloader
from .community_meteorology_downloader import CommunityMeteorologyDownloader
from .community_meteorology_helper import CommunityMeteorologyHelper

class MeteorologyInitialLoader():
    def __init__(self, meteorology_configuration:MeteorologyConfiguration, api_client:ApiClient, logger:Logger) -> None:
        self.__meteorology_configuration__ :MeteorologyConfiguration = meteorology_configuration
        self.__api_client__ :ApiClient = api_client
        self.__logger__ :Logger = logger

    # Realiza la carga inicial de los datos
    def load(self) -> None:
        self.__logger__.info('Meteorology initial loader starts')
        meteorology_downloader = MeteorologyDownloader(self.__meteorology_configuration__, self.__api_client__, self.__logger__)
        meteorology_downloader.get_available_files()
        helper = MeteorologyHelper(self.__api_client__, self.__logger__)
        measurement_parser = MeasurementParser(self.__api_client__, self.__logger__, helper)
        measurement_parser.upload_all_files(self.__meteorology_configuration__.download_path)

        #Comunidad
        community_meteorology_downloader: CommunityMeteorologyDownloader = CommunityMeteorologyDownloader(self.__meteorology_configuration__,self.__api_client__, self.__logger__)
        community_meteorology_downloader.get_available_files()

        helper = CommunityMeteorologyHelper(self.__api_client__, self.__logger__)
        measurement_parser = MeasurementParser(self.__api_client__, self.__logger__, helper)
        measurement_parser.upload_all_files(self.__meteorology_configuration__.community_download_path)

    


