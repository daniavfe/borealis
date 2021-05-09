from configuration import *
from client import ApiClient
from common import Logger
from traffic import TrafficPointDownloader


# Configuración y dependencias
configuration :Configuration = Configuration.load_from_file('configuration.development.json')

#Cliente de la API
api_client :ApiClient = ApiClient(configuration.api)

#Logger
logger :Logger = Logger()

traffic :TrafficPointDownloader = TrafficPointDownloader()
