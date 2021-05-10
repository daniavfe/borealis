from .measurement_analyzer import MeasurementAnalyzer
from client import ApiClient
from common import Logger

class Helper():
    def __init__(self, api_client:ApiClient, logger:Logger):
        raise Exception('Not implemented method')

    def get_extension(self):
        raise Exception('Not implemented method')

    def get_section_size(self):
        raise Exception('Not implemented method')

    def get_thread_number(self):
        raise Exception('Not implemented method')

    def get_usable_file_content(self, file_path:str):
        raise Exception('Not implemented method')

    def get_data_content(self, row:object):
        raise Exception('Not implemented method')

    def upload_data(self, items_to_upload:list):
        raise Exception('Not implemented method')

    def pre_upload(self):
        raise Exception('Not implemented method')
    