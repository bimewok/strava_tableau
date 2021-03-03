import gpxpy
import gpxpy.gpx
import pandas as pd
import geopandas as gpd
from shapely.geometry import LineString

tabular = pd.read_csv(r'C:\garrett_workspace\tableau\strava_dashboard\activities.csv')

geo_dataframe = gpd.GeoDataFrame(tabular)
geo_dataframe['geometry'] = None



for index in range(len(geo_dataframe)):
    filepath = geo_dataframe['gpx_filepath'][index]
    file = open(filepath, 'r')
    gpx = gpxpy.parse(file)
    
    points = []
    elev = []
    
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                points.append(tuple([point.longitude, point.latitude]))
                elev.append(int(point.elevation*3.28))
    line = LineString(points)
    geo_dataframe.loc[index, 'geometry'] = line
    print(index+1,'files parsed.')    
    


geo_dataframe.to_file(r'C:\garrett_workspace\tableau\strava_dashboard\geo_dataframe.shp')

crs_to_write = """GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]]"""


with open(r'C:\garrett_workspace\tableau\strava_dashboard\{}.prj'.format('geo_dataframe'), 'w') as file:
    file.write(crs_to_write)