import requests
import json
import sys
from magnitude_parser import MagnitudeParser
from station_parser import StationParser

#magnitude_parser = MagnitudeParser()
#magnitude_parser.load('data/magnitudes.csv');

station_parser = StationParser()
station_parser.load('data/stations.csv')
