from density import *

#density_downloader = DensityDownloader('data/density')
#density_downloader.download_density_file(range(2001, 2020))

density_parser = DensityParser()
density_parser.__load_file__('data/density/2012/all.csv');

