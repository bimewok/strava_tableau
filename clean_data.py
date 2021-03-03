import geopandas as gpd
import pandas as pd
import numpy as np



data = gpd.read_file(r'C:\garrett_workspace\tableau\strava_dashboard\strava_dashboard.shp')

data = data[['Activity I', 'Activity D', 'Activity N', 'Activity T', 'Elapsed Ti', 
             'Distance', 'Moving Tim', 'Average Sp',
             'Elevation', 'Elevatio_1', 'Elevatio_2', 'Elevatio_3', 'Calories', 'geometry']]

data.columns = ['id', 'date', 'name', 'type', 'duration', 'distance', 'moving_time', 
                'avg_speed', 'elev_gain', 'elev_1', 'elev_2', 'elev_3', 'calories', 'geometry']


data['date'] = (pd.to_datetime(data['date'])).astype('str')
data['duration'] = data['duration'] / 60 / 60


data['distance'] = data['distance'] * 0.6213
data['moving_time'] = data['moving_time'] / 60 / 60
data['avg_speed'] = data['distance'] / data['moving_time']

data['elev_gain'] = data['elev_gain'].fillna(data['elev_3'] - data['elev_2']).fillna(0)

data = data.drop(['elev_1', 'elev_2', 'elev_3'], axis=1)

data['elev_gain'] = (data['elev_gain'] * 3.28).astype('int')



filename = 'activities_data'

data.to_file(r'C:\garrett_workspace\tableau\strava_dashboard\{}.shp'.format(filename))

crs_to_write = """GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]]"""


with open(r'C:\garrett_workspace\tableau\strava_dashboard\{}.prj'.format(filename), 'w') as file:
    file.write(crs_to_write)