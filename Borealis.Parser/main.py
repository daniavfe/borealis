from density import *
from holiday import *
from meteorology import *
from pollution import *
from common import *

#Carga inicial de densidades
#density_downloader = DensityDownloader('data/density')
#density_downloader.download_density_file(range(2001, 2020))
#density_parser = DensityParser()
#density_parser.__load_file__('data/density/2012/all.csv');

#Carga mensual de densidades

#Carga inicial de vacaciones

#holiday_downloader = HolidayDownloader('https://datos.madrid.es/sites/v/index.jsp?vgnextoid=9f710c96da3f9510VgnVCM2000001f4a900aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD','data/holiday')
#holiday_downloader.download_calendar()

#holiday_parser = HolidayParser()
#holiday_parser.load_file('data/holiday/calendar.csv')

#Carga inicial de meteo

#meteorology_downloder = MeteorologyDownloader('https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=fa8357cec5efa610VgnVCM1000001d4a900aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default', 'data/meteorology')
#meteorology_downloder.get_available_files()

#meteorology_parser = MeteorologyParser(10, 70)
#meteorology_parser.load_with_parallelism('data/meteorology/2019/2019.txt')


#Carga inicial de pollution

#pollution_downloader = PollutionDownloader('https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=f3c0f7d512273410VgnVCM2000000c205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default', 'data/measurements');
#pollution_downloader.get_available_files()

pollution_parser = PollutionParser(20, 30)
pollution_parser.load_with_parallelism('data/measurements/2001/Ene_mo01.txt')

#Análisis de measurements

#measurement_analyzer = MeasurementAnalyzer()
#station_ids, magnitude_ids = measurement_analyzer.analyze_all_files_in_directory('data/measurements')