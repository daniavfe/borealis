import os, glob
from measurement_parser import MeasurementParser



class MeasurementAnalyzer():

    def analyze_all_files_in_directory(self, path):
        if not os.path.isdir(path):
            print(f'Path {path} is not a directory')
            return
         
        total_station_ids = set()
        total_magnitude_ids = set()
        
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".txt"):
                    station_ids= self.analyze_file(os.path.join(root, file))
                    total_station_ids.update(station_ids)
                    print(f'{root} {file}')
        print(f'stations: {sorted(total_station_ids)}')

    def analyze_file(self, path):
        if not os.path.isfile(path):
            print(f'File {path} is not valid')
            return
        return self.__analyze__(path)
    
    def __analyze__(self, path):
        station_ids = set()

        if not os.path.isfile(path):
            print(f'File {path}')
            return

        file = open(path, 'r')
        content = file.readlines()
        number_of_lines = len(content)
        number_of_processed_lines = 0
        
        print(f'Analyzing {path}')
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

            mag = station_id
            station_ids.add(mag)
            number_of_processed_lines += 1
        
        print(f'Analysis done')
        return station_ids