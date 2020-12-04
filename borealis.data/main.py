from datetime import datetime, timedelta
import requests
import json
import sys

file = open('data/2001/Ene_mo01.txt', 'r')
lines = file.readlines()

number_of_items = len(lines)
number_of_processedItems = 0
percentage = 0.0

# Strips the newline character
for line in lines:
    province = line[0:2]
    town = line[2:5]
    station = line[5:8]
    magnitude = line[8:10]
    method = line[10:12]
    analysis_period = line[12:14]
    date = datetime(int("20"+line[14:16]), int(line[16:18]), int(line[18:20]))

    count = 0

    while count < 24:
        index = 20 + (count * 6)
        data = line[index: index+5]
        validation_code = line[index+5:index+6]
        count += 1
        measurementDatetime = date + timedelta(hours=count)

        payload = {"province": province, "town": town, "station": station,
                   "datetime": measurementDatetime.strftime("%Y-%m-%d %H:%M:%S"), "magnitude": magnitude,
                   "method": method, "analysis_period": analysis_period,
                   "data": data, "validation_code": validation_code}

        requests.post("http://127.0.0.1:5000/api/measurement", data=json.dumps(payload))

    number_of_processedItems += 1
    percentage = number_of_processedItems / number_of_items * 100
    sys.stdout.flush()
    print(f'{percentage} %')



