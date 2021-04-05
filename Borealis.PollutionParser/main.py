import requests
import json
import sys
from magnitude_parser import MagnitudeParser
from station_parser import StationParser
from measurement_parser import MeasurementParser
from measurement_downloader import MeasurementDownloader
from measurement_analyzer import MeasurementAnalyzer

#magnitude_parser = MagnitudeParser()
#magnitude_parser.load('data/magnitudes.csv')

#station_parser = StationParser()
#station_parser.load('data/stations.csv')

measurement_parser = MeasurementParser()
measurement_parser.load('data/measurements/2001/Ene_mo01.txt')

#measurement_downloader = MeasurementDownloader("https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=f3c0f7d512273410VgnVCM2000000c205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default", "data/measurements/")
#measurement_downloader.get_available_files()

#measurement_analyzer = MeasurementAnalyzer()

#measurement_analyzer.analyze_all_files_in_directory("data/measurements")


