from client import ApiClient
from common import Logger
from .helper import Helper
from datetime import datetime
import threading
import os
import math

class MeasurementParser():
  
    def __init__(self, api_client:ApiClient, logger:Logger, helper:Helper) -> None:
        self.__api_client__ :ApiClient = api_client
        self.__logger__ :Logger = logger
        self.__measurement_helper__ : Helper = helper
    
    def upload_all_files(self, path:str) -> None:
        if not os.path.isdir(path):
            self.__logger__.info(f'Path {path} is not a directory')
            return
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(self.__measurement_helper__.get_extension()):
                    timeline_id = file.split('-')[0]
                    self.__api_client__.update_timeline(timeline_id, 'Uploading')
                    self.load_with_parallelism(os.path.join(root, file))
                    self.__api_client__.update_timeline(timeline_id, 'Uploaded')

    def load_with_parallelism(self, file_path:str, section_size:int=20, thread_number:int=30) -> None:
        # Index initialization
        self.__section__index = 0
        # Mutex for index
        self.__section_lock__ = threading.Lock()
        # Size of section to process by each tread
        self.__section_size__ = section_size
        # Number of threads
        self.__thread_number__ = thread_number
        # Processing start date
        start_date = datetime.utcnow()

        # Get usable file content
        self.__file_content__ = self.__measurement_helper__.get_usable_file_content(file_path)

        # Obtain the number of sections by section size
        self.__number_of_sections__ = math.floor(len(self.__file_content__) / self.__section_size__)

        # Get file length
        size = len(self.__file_content__)

        # Print thread information
        self.__logger__.info(f'Uploading file {file_path}.Size: {size}. Section size: {self.__section_size__}. Nº of sections: {self.__number_of_sections__}. Thread number: {self.__thread_number__}')
       

        #Before start to upload we call this function
        self.__measurement_helper__.pre_upload(file_path)
        
        # Inititalize thread data structure
        threads = [threading.Thread] * self.__thread_number__

        # Inititalize and start threads
        for index in range(0, self.__thread_number__):
            i = index
            threads[index] = threading.Thread(target = self.__process_item__, args = [i])
            threads[index].start()

        # Wait for all threads to end
        for index in range(0, self.__thread_number__):
            threads[index].join()
        
        # Processing end date
        end_date = datetime.utcnow()
  
    def __process_item__(self, thread_number:int) -> None:
        self.__logger__.debug(f"Tread {thread_number} started")

        # Get the section of file to be proccesed by this thread
        section_content = self.__get_section_content__()

        # Threshold to upload data
        items_to_upload_threshold = 100
        items_to_upload = []

        # Main loop, while content is provided, process it
        while(section_content != None):      
            for row in section_content:
                # Get data for uploading
                data = self.__measurement_helper__.get_data_content(row)
                items_to_upload.extend(data)
      
                # If threshold has been overcome, upload it
                if len(items_to_upload) >= items_to_upload_threshold:
                    self.__measurement_helper__.upload_data(items_to_upload)
                    items_to_upload.clear()
             
            # If items left in colelction, upload them
            if len(items_to_upload) > 0:
                self.__measurement_helper__.upload_data(items_to_upload)

            section_content = self.__get_section_content__()
        self.__logger__.debug(f"Thread {thread_number} finished")

    #devuelve la sección correspondiente al fichero que tiene que procesar
    def __get_section_content__(self) -> list:
        self.__section_lock__.acquire()
        if(self.__section__index > self.__number_of_sections__):
            self.__section_lock__.release()
            return None

        start_element_index = self.__section__index * self.__section_size__
        posible_end_element_index = ((self.__section__index + 1) * self.__section_size__)

        if(posible_end_element_index >= len(self.__file_content__)):
            end_element_index = len(self.__file_content__)
        else:     
            end_element_index = posible_end_element_index

        self.__logger__.debug(f'start: {start_element_index}, end:{end_element_index}')

        self.__section__index += 1

        self.__section_lock__.release()

        return self.__file_content__[start_element_index:end_element_index]


