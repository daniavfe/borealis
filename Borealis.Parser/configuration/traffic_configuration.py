class TrafficConfiguration():
    def __init__(self, point_page_url:str, measurement_page_url:str, download_path:str) -> None:
        self.point_page_url :str = point_page_url
        self.measurement_page_url :str = measurement_page_url
        self.download_path :str = download_path


