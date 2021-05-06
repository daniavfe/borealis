from .meteorology_downloader import MeteorologyDownloader
from measurement import MeasurementParser
from configuration import MeteorologyConfiguration
from client import ApiClient

class MeteorologyInitialLoad():
    def __init__(self, meteorology_configuration:MeteorologyConfiguration, api_client:ApiClient) -> None:
        self.__meteorology_configuration__ :MeteorologyConfiguration = meteorology_configuration
        self.__api_client__ :ApiClient = api_client

    # Realiza la carga inicial de los datos
    def load(self)->None:
        meteorology_downloader = MeteorologyDownloader(self.__meteorology_configuration__)
        meteorology_downloader.get_available_files()
        measurement_parser = MeasurementParser(self.__api_client__)
        measurement_parser.upload_all_files('data/meteorology')

    


