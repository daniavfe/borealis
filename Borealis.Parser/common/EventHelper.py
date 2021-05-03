import requests

class EventHelper():
    
    def __init__(self):
        self.__api_url__ = 'http://127.0.0.1:5000/api/'
        self.__event_log_endpoint__ = 'event/log'
        self.__event_filedownload_endpoint__ = 'event/filedownload'
        self.__event_fileupload_endpoint__ = 'event/fileupload'

    def log_event(self, message):
        payload = {'message': message}
        requests.post(f'{self.__api_url__}{self.__event_log_endpoint__}', data=json.dumps(payload)).content

    def file_download_event(self, file_name, file_size):
         payload = {'fileName': file_name, 'fileSize': file_size}
         requests.post(f'{self.__api_url__}{self.__event_filedownload_endpoint__}', data=json.dumps(payload)).content

    def file_upload_event(self, file_id, file_name, upload_progress):
          payload = {'fileId':file_id, 'fileName': file_name, 'uploadProgress': upload_progress}
          requests.post(f'{self.__api_url__}{self.__event_fileupload_endpoint__}', data=json.dumps(payload)).content
