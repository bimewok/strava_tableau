import geopandas as gpd

data = gpd.read_file(r'C:\garrett_workspace\tableau\strava_dashboard\activities_data.shp')

resample_factor = 4

for row in range(len(data)):
    '''the try - except block is because I added dummy null rows to represent weeks
    that I had no activities, thus these rows have no geometry...'''
    try:
        linestring = data['geometry'][row]
        simplified_points = []
        for i in range(len(linestring.coords)):
            coord = linestring.coords[i]
            if i % resample_factor == 0:
                simplified_points.append(coord)
        data['geometry'][row].coords = simplified_points
    except: 
        pass
    
data.to_file(r'C:\garrett_workspace\tableau\strava_dashboard\{}.shp'.format('activities_data'))

