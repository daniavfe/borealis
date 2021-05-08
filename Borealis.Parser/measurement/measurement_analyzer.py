from common import Logger
import os, glob

class MeasurementAnalyzer():

    def __init__(self, logger:Logger):
        self.__logger__ = logger

    def analyze_all_files_in_directory(self, path):
        if not os.path.isdir(path):
            self.__logger__.warning(f'Path {path} is not a directory')
            return
         
        total_station_ids = set()
        total_magnitude_ids = set()
        
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".txt"):
                    station_ids, magnitude_ids= self.analyze_file(os.path.join(root, file))
                    total_station_ids.update(station_ids)
                    total_magnitude_ids.update(magnitude_ids)
                    print(f'{root} {file}')
        self.__logger__.info(f'stations: {sorted(total_station_ids)}')
        elf.__logger__.info(f'magnitudes: {sorted(total_magnitude_ids)}')
        return total_station_ids, total_magnitude_ids

    def analyze_file(self, path):
        if not os.path.isfile(path):
            elf.__logger__.error(f'File {path} is not valid')
            return
        return self.__analyze__(path)
    
    def __analyze__(self, path):
        station_ids = set()
        magnitude_ids = set()
        if not os.path.isfile(path):
            self.__logger__.warning(f'File {path}')
            return

        file = open(path, 'r')
        content = file.readlines()
        number_of_lines = len(content)
        number_of_processed_lines = 0
        
        self.__logger__.info(f'Analyzing {path}')
        for line in content:
            station_id = -1
            magnitude_id = -1
            if line[2] == ',':
                component = line.split(',')
                station_id = component[2]
                magnitude_id = component[3]
                technique_id = component[4]
            else:
                station_id = line[5:8]
                magnitude_id = line[8:10]
                technique_id = line[10:12]

            station_ids.add(station_id)
            magnitude_ids.add(magnitude_id)
            number_of_processed_lines += 1
        
        self.__logger__.info(f'Analysis done')
        return station_ids, magnitude_ids