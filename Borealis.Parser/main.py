from configuration import *
from client import ApiClient


# Configuración y dependencias
configuration :Configuration = Configuration.load_from_file('configuration.development.json')

#Cliente de la API
api_client :ApiClient = ApiClient(configuration.api)

response = api_client.get_last_timeline("Density");
x=1
