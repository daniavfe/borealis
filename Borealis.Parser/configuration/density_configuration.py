class DensityConfiguration():
    def __init__(self, main_page_url:str,community_main_page_url :str, data_page_url:str,community_data_page_url :str, download_path:str, community_download_path:str) -> None:
        self.main_page_url :str = main_page_url
        self.community_main_page_url :str = community_main_page_url
        self.data_page_url :str = data_page_url
        self.community_data_page_url :str = community_data_page_url
        self.download_path :str = download_path
        self.community_download_path:str = community_download_path
