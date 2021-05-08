from .density_downloader import DensityDownloader
from .density_parser import DensityParser
from configuration import DensityConfiguration
from common import Logger
from client import ApiClient

class DensityInitialLoader():
    def __init__(self, configuration:DensityConfiguration, api_client:ApiClient, logger:Logger) -> None:
        self.__configuration__ :DensityConfiguration = configuration
        self.__api_client__ :ApiClient = api_client
        self.__logger__ :Logger = logger

    # Realiza la carga inicial de los datos
    def load(self) -> None:
        self.__logger__.info('Density initial loader starts');
        density_downloader = DensityDownloader(self.__configuration__, self.__logger__)
        density_downloader.download_density_file()
        density_parser = DensityParser(self.__api_client__, self.__logger__)
        density_parser.upload_all_files('data/density')


    


