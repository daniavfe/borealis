from .traffic_point_downloader import TrafficPointDownloader
from configuration import TrafficConfiguration
from client import ApiClient
from common import Logger

class TrafficInitialLoader():
    def __init__(self, traffic_configuration:TrafficConfiguration, api_client:ApiClient, logger:Logger) -> None:
        self.__traffic_configuration__ :TrafficConfiguration = traffic_configuration
        self.__api_client__ :ApiClient = api_client
        self.__logger__:Logger = logger

    # Realiza la carga inicial de los datos
    def load(self)->None:
        traffic_point_downloader = TrafficPointDownloader(self.__traffic_configuration__,self.__api_client__, self.__logger__)
        traffic_point_downloader.get_available_files()



