from .density_downloader import DensityDownloader
from .density_parser import DensityParser
from configuration import DensityConfiguration
from common import Logger
from client import ApiClient


class DensityContinuousLoader():
    def __init__(self, configuration:DensityConfiguration, api_client:ApiClient, logger:Logger) -> None:
        self.__configuration__ :DensityConfiguration = configuration
        self.__api_client__ :ApiClient = api_client
        self.__logger__ :Logger = logger

    # Realiza la carga inicial de los datos
    def load(self) -> None:
        self.__logger__.info('Density continuous loader starts');

