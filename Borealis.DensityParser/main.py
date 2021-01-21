from bs4 import BeautifulSoup
import requests
import datetime
import csv


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
        return list(map(lambda x:getDataValuesFromTable(x), table));
    except:
        return [];


district_list, year_list = getDitrictsAndYears()
final_list = [];
for district in district_list:
    for year in year_list:
        month_list, zone_list = getAvailableMonthsAndZones(year, district)
        for month in month_list:
            densities = getDensity(year, district, month, zone_list);
            for density in densities:
                month_number = int(month[0:2]);
                final_list.append({'year': year, 'month':month, 'district':district[3:], 'zone':density[0], 'value': density[1]});

            print(f'{district} {year}-{month}');


keys = final_list[0].keys();
with open('density.csv', 'w', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(final_list)

print(f'Listo');
