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
                    station_ids, magnitude_ids = self.analyze_file(os.path.join(root, file))
                    total_magnitude_ids.update(magnitude_ids)
                    total_station_ids.update(station_ids)
                    print(f'{root} {file}')
        print(f'stations: {total_station_ids}')
        print(f'magnitudes: {total_magnitude_ids}')

    def analyze_file(self, path):
        if not os.path.isfile(path):
            print(f'File {path} is not valid')
            return
        return self.__analyze__(path)
    
    def __analyze__(self, path):
        magnitude_ids = set()
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
            else:
                station_id = int(line[5:8])
                magnitude_id = int(line[8:10])

            station_ids.add(station_id)
            magnitude_ids.add(magnitude_id)
            number_of_processed_lines += 1
        
        print(f'Analysis done')
        return station_ids, magnitude_ids