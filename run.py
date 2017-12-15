import pandas as pd
import os
import wikipedia
import json

wikipedia.set_lang("de")
path = "C:\\Users\\PaulBauriegel\\Downloads\\20171212_wifionice\\surveyor_hackathon_data_20171212.csv"
df = pd.read_csv(path, sep=';', decimal='.', skiprows=0, nrows=100)    # Read one row
df = df[df['sid'] == 40117905]
df = df.filter(items=['gps_breite', 'gps_laenge'])
df.rename(columns={'gps_laenge': 'longitude', 'gps_breite': 'latitude'}, inplace=True)
pois = wikipedia.geosearch(df.iloc[0]['latitude'], df.iloc[0]['longitude'])
print(pois)