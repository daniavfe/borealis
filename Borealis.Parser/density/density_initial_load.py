from .density_downloader import DensityDownloader
from .density_parser import DensityParser
from configuration import DensityConfiguration
from common import EventHelper
from client import ApiClient

class DensityInitialLoad():
    def __init__(self, configuration:DensityConfiguration, api_client:ApiClient) -> None:
        self.__configuration__ :DensityConfiguration = configuration
        self.__api_client__ :ApiClient = api_client

    # Realiza la carga inicial de los datos
    def load(self)->None:
        density_downloader = DensityDownloader(self.__configuration__)
        density_downloader.download_density_file()
        density_parser = DensityParser(self.__api_client__)
        density_parser.upload_all_files('data/density')


    


