from datetime import datetime, timedelta
import csv
import json
import requests

station_url = 'https://datos.madrid.es/egob/catalogo/212629-1-estaciones-control-aire.csv'

def get_station_file():
    response = requests.get(station_url)
    open('data/stations.csv', 'wb').write(response.content)
    return response.content

def insert_station(id, name, address, start_date, latitude, longitude, altitude):
    payload = {"id":id, "name":name, "address":address, "start_date":start_date, "latitude":latitude, "longitude":longitude, "altitude": altitude}
    return requests.post("http://127.0.0.1:5000/api/pollution/station/", data=json.dumps(payload)).content


def insert_station_magnitude(station_id, magnitude_id):
    payload = {"station_id":station_id, "magnitude_id":magnitude_id}
    return requests.post("http://127.0.0.1:5000/api/pollution/station/magnitude", data=json.dumps(payload)).content


get_station_file()
with open('data/stations.csv') as input_file:
    csv_reader = csv.reader(input_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            id = int(row[1])
            name = row[2]
            address= row[3]
            start_date= datetime.strptime(row[21], '%d/%m/%Y').strftime('%Y-%m-%d %H:%M:%S')
            longitude = row[24]
            latitude = row[25]
            altitude = int(row[6])
            insert_station(id, name, address, start_date, latitude, longitude, altitude)
            line_count += 1

    print(f'Done!')