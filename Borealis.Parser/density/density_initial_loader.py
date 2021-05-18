from measurement import MeasurementParser
from configuration import DensityConfiguration
from common import Logger
from client import ApiClient
from .density_downloader import DensityDownloader
from .density_helper import DensityHelper

class DensityInitialLoader():
    def __init__(self, density_configuration:DensityConfiguration, api_client:ApiClient, logger:Logger) -> None:
        self.__density_configuration__ :DensityConfiguration = density_configuration
        self.__api_client__ :ApiClient = api_client
        self.__logger__ :Logger = logger

    # Realiza la carga inicial de los datos
    def load(self) -> None:
        #self.__logger__.info('Density initial loader starts')
        density_downloader = DensityDownloader(self.__density_configuration__, self.__api_client__, self.__logger__)
        density_downloader.download_density_file()
        helper = DensityHelper(self.__api_client__, self.__logger__)
        measurement_parser = MeasurementParser(self.__api_client__, self.__logger__, helper)
        measurement_parser.upload_all_files(self.__density_configuration__.download_path)


    


