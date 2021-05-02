from meteorology_downloader import MeteorologyDownloader
from meteorology_parser import MeteorologyParser

#meteorology_downloader = MeteorologyDownloader("https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=fa8357cec5efa610VgnVCM1000001d4a900aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default", "data/meteorology/")
#meteorology_downloader.get_available_files()

meteorology_parser = MeteorologyParser(10, 70)
meteorology_parser.load_with_parallelism('data/meteorology/2019/2019.txt')
