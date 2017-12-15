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
    print(pois)
    gjson['pois'] = pois
    return jsonify(dict(gjson))