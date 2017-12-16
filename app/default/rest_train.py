import pandas as pd
from . import default
import wikipedia
import json
from flask import jsonify
import re
import os

df = 0
wikipedia.set_lang("de")


def init():
    path = os.path.dirname(os.path.abspath(__file__)) + "/surveyor_hackathon_data_20171212.csv"
    global df
    df = pd.read_csv(path, sep=';', decimal='.', skiprows=0, nrows=100)  # Read one row
    df = df.filter(items=['sid', 'gps_breite', 'gps_laenge'])
    df.rename(columns={'gps_laenge': 'trainLongitude', 'gps_breite': 'trainLatitude'}, inplace=True)
    # TODO sort by time


def get_first_image(wikipedia_page):
    htmlcode = wikipedia_page.html()
    try:
        imgcode = re.search('<img.*src=".*".*/>', htmlcode).group(0)
    except:
        return ''
    imagecode_array = imgcode.split()
    for imagecode_part in imagecode_array:
        if "src=" in imagecode_part:
            imagecode_array = imagecode_part.split('"')
            break
    for imagecode_part in imagecode_array:
        if "//" in imagecode_part:
            image_url = "https:"+ imagecode_part.split("thumb/")[0] + imagecode_part.split("thumb/")[1].rsplit("/",1)[0]
            return image_url


@default.route('/gps/<int:trainid>/<int:time>')
def browse(trainid, time):
    global df
    df_temp = df[df['sid'] == trainid]
    gjson = df_temp.iloc[time].to_dict()
    pois = wikipedia.geosearch(df_temp.iloc[time]['trainLatitude'], df_temp.iloc[time]['trainLongitude'])
    poi_list = []
    for e in pois:
        npoi = {}
        urls = []
        npoi['name'] = e
        info = wikipedia.page(e)
        npoi['description'] = info.summary
        npoi['latitude'] = float(info.coordinates[0])
        npoi['longitude'] = float(info.coordinates[1])
        npoi['imageUrl'] = get_first_image(info)
        urls.append(info.url)
        npoi['linkUrls'] = urls
        poi_list.append(npoi)
    gjson['pois'] = poi_list
    return jsonify(dict(gjson))

