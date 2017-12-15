import pandas as pd
from . import default
import wikipedia
import json
from flask import jsonify

wikipedia.set_lang("de")

@default.route('/gps/<int:trainid>/<int:time>')
def browse(trainid, time):
    path = "C:\\Users\\PaulBauriegel\\Downloads\\20171212_wifionice\\surveyor_hackathon_data_20171212.csv"
    df = pd.read_csv(path, sep=';', decimal='.', skiprows=0, nrows=100)    # Read one row
    df = df[df['sid'] == trainid]
    df = df.filter(items=['gps_breite', 'gps_laenge'])
    df.rename(columns={'gps_laenge': 'trainLongitude', 'gps_breite': 'trainLatitude'}, inplace=True)
    gjson = df.iloc[time].to_dict()
    pois = wikipedia.geosearch(df.iloc[time]['trainLatitude'], df.iloc[time]['trainLongitude'])
    poi_list = []
    for e in pois:
        npoi = {}
        npoi['name'] = e
        npoi['description'] = wikipedia.summary(e)
        info = limburgerDom = wikipedia.page(e)
        npoi['latitude'] = float(info.coordinates[0])
        npoi['longitude'] = float(info.coordinates[1])
        poi_list.append(npoi)
    gjson['pois'] = poi_list
    return jsonify(dict(gjson))