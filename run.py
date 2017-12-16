import pandas as pd
import os
import wikipedia
import json

wikipedia.set_lang("de")
path = os.path.dirname(os.path.abspath(__file__)) + "/app/default/surveyor_hackathon_data_20171212.csv"
df = pd.read_csv(path, sep=';', decimal='.', skiprows=0, nrows=1)    # Read one row
df = df[df['sid'] == 40117905]
df = df.filter(items=['gps_breite', 'gps_laenge'])
df.rename(columns={'gps_laenge': 'longitude', 'gps_breite': 'latitude'}, inplace=True)
pois = wikipedia.geosearch(df.iloc[0]['latitude'], df.iloc[0]['longitude'])
poi_list = []
for e in pois:
    npoi = {}
    npoi['name'] = e
    npoi['description'] = wikipedia.summary(e)
    info = limburgerDom = wikipedia.page(e)
    npoi['latitude'] = info.coordinates[0]
    npoi['longitude'] = info.coordinates[1]
    poi_list.append(npoi)
print(poi_list)