import webbrowser
import pandas as pd
import time
import numpy as np
from os import listdir
import os.path


chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))


for file in listdir(r'C:\garrett_workspace\tableau\strava_dashboard\gpx'):
    os.remove(r'C:\garrett_workspace\tableau\strava_dashboard\gpx\{}'.format(file))



activity_data = pd.read_csv(r'C:\garrett_workspace\Strava_Backup_Data\activities.csv')
# activity_data = activity_data.tail(3).reset_index()
activity_data['gpx_filepath'] = np.nan



full_file_names = []

for i in range(len(activity_data)):
    if activity_data['Filename'][i] != np.nan:
        activity_id = int(activity_data['Activity ID'][i])
        url = 'https://www.strava.com/activities/{}/export_gpx'.format(activity_id)
        webbrowser.get('chrome').open_new_tab(url)
        time.sleep(15)
        for z in range(1, 30000):
            files = listdir(r'C:\garrett_workspace\tableau\strava_dashboard\gpx')
            for x in files:
                if 'Unconfirmed' in x:
                    time.sleep(1)
                else:
                    pass



        for file in files:
            full_file_names.append(r'C:\garrett_workspace\tableau\strava_dashboard\gpx\{}'.format(file))
        latest_file = max(full_file_names, key=os.path.getctime)
        activity_data.loc[i, 'gpx_filepath'] = str(latest_file)
        
activity_data.to_csv(r'C:\garrett_workspace\Strava_Backup_Data\activities.csv')