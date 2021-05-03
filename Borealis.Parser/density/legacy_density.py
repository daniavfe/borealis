from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests
import csv
import json


#request to web page
page_url = 'http://www-2.munimadrid.es/TSE6/control/seleccionDatosBarrio'
data_url = 'http://www-2.munimadrid.es/TSE6/control/mostrarDatos'

def getDitrictsAndYears():
    response = requests.get(page_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    district_list = list(map(lambda x:x['value'].strip(), soup.find(attrs={"name" : "selectDistrito"}).findChildren()))[1:];
    year_list=list(map(lambda x:int(x['value'].strip()), soup.find(attrs={"name" : "selectAnio"}).findChildren()));
    return district_list, year_list;

def getAvailableMonthsAndZones(year, district):
    data = {'barrioSeccion':'Barrio','nombreSerie':'Población por distrito y barrio','selectAnio':year,'selectMes':'','selectDistrito':district,
            'selectEdad':'00', 'selectTramoEdad':'', 'selectNacionalidad':'03', 'selectSexo':'03', 'selectTipoDato':'01', 'selectTipoPorcentaje':'', 'Consultar':'Consultar'};
    response = requests.post(page_url, data=data);

    soup = BeautifulSoup(response.content, 'html.parser');
    month_list = list(map(lambda x:x['value'].strip(), soup.find(attrs={"name" : "selectMes"}).findChildren()));
    zone_list = list(map(lambda x:x['value'].strip(), soup.find(attrs={"name" : "selectBarrio"}).findChildren()))[1:];
    return month_list, zone_list;    

def getDataValuesFromTable(item):
    itemKey = item.find('td', {"class" : "CabTab0"}).text.split('/')[1].strip();
    itemValue = int(item.find('td', {"class" : "DatTab"}).text.replace('.', ''));
    return itemKey, itemValue

def getDensity(year, district, month, zones):
    data = {'barrioSeccion':'Barrio','nombreSerie':'Población por distrito y barrio','selectAnio':year,'selectMes':month,'selectDistrito':district, 'selectBarrio':zones,
            'selectEdad':'00', 'selectTramoEdad':'', 'selectNacionalidad':'03', 'selectSexo':'03', 'selectTipoDato':'01', 'selectTipoPorcentaje':'', 'Consultar':'Consultar'};
    response = requests.post(data_url, data=data);

    soup = BeautifulSoup(response.content, 'html.parser');
    try:
        table =  soup.find_all('table')[1].findChildren('tr')[2:];
        return list(set(map(lambda x:getDataValuesFromTable(x), table)));
    except:
        return [];

def insertDistrict(name):
    payload = {"name": name, "surface":0.0}
    return int(requests.post("http://127.0.0.1:5000/api/density/district", data=json.dumps(payload)).content)

def insertNeighborhood(districtId, name):
    payload = {"districtId":districtId, "name":name, "surface":0.0}
    return int(requests.post("http://127.0.0.1:5000/api/density/neighborhood", data=json.dumps(payload)).content)

def insertDensity(districtId, neighborhoodId, year, month, value):
    payload = {"districtId":districtId, "neighborhoodId":neighborhoodId, "year":year, "month":month, "value":value}
    response = requests.post("http://127.0.0.1:5000/api/density", data=json.dumps(payload));
    x = response

district_list, year_list = getDitrictsAndYears()
final_list = []

district_id_list = dict()
neighborhood_id_list = dict()


for district in district_list:
    districtId = 0
    if(not district[3:] in district_id_list):
        districtId = insertDistrict(district[3:])
        district_id_list[district[3:]] = districtId
    else:
        districtId =  district_id_list[district[3:]]

    for year in year_list:
        month_list, zone_list = getAvailableMonthsAndZones(year, district)      
        for month in month_list:
            densities = getDensity(year, district, month, zone_list);
            for density in densities: 
                neighborhoodId = 0
                if(not density[0] in neighborhood_id_list):
                    neighborhoodId = insertNeighborhood(districtId, density[0])
                    neighborhood_id_list[density[0]] = neighborhoodId
                else:
                     neighborhoodId = neighborhood_id_list[density[0]]

                month_number = int(month[0:2]);
                insertDensity(districtId, neighborhoodId, year, month_number, density[1])          
                final_list.append({'year': year, 'month':month_number, 'district':district[3:], 'zone':density[0], 'value': density[1]})
            print(f'{district} {year}-{month}')



keys = final_list[0].keys();
with open('density.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(final_list)

print(f'Listo');
