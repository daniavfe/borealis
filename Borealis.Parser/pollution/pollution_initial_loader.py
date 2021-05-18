from measurement import MeasurementParser
from configuration import PollutionConfiguration
from client import ApiClient
from common import Logger
from .pollution_downloader import PollutionDownloader
from .pollution_helper import PollutionHelper
from .community_pollution_downloader import CommunityPollutionDownloader
from .community_pollution_helper import CommunityPollutionHelper


class PollutionInitialLoader():
    def __init__(self, pollution_configuration:PollutionConfiguration, api_client:ApiClient, logger:Logger) -> None:
        self.__pollution_configuration__ :PollutionConfiguration = pollution_configuration
        self.__api_client__ :ApiClient = api_client
        self.__logger__:Logger = logger

    # Realiza la carga inicial de los datos
    def load(self)->None:
        #pollution_downloader = PollutionDownloader(self.__pollution_configuration__,self.__api_client__, self.__logger__)
        #pollution_downloader.get_available_files()
        #helper = PollutionHelper(self.__api_client__, self.__logger__)
        #measurement_parser = MeasurementParser(self.__api_client__, self.__logger__, helper)
        #measurement_parser.upload_all_files(self.__pollution_configuration__.download_path)

        #Comunidad
        community_pollution_downloader: CommunityPollutionDownloader = CommunityPollutionDownloader(self.__pollution_configuration__,self.__api_client__, self.__logger__)
        community_pollution_downloader.get_available_files()

        helper = CommunityPollutionHelper(self.__api_client__, self.__logger__)
        measurement_parser = MeasurementParser(self.__api_client__, self.__logger__, helper)
        measurement_parser.upload_all_files(self.__pollution_configuration__.community_download_path)
