import pandas as pd
from app.default import default
import wikipedia
import json
from flask import jsonify
import re
import os
import multiprocessing
import requests


df = 0
wikipedia.set_lang("de")


def init():
    path = os.path.dirname(os.path.abspath(__file__)) + "/surveyor_hackathon_data_20171212.csv"
    global df
    df = pd.read_csv(path, sep=';', decimal='.', skiprows=0, nrows=100000)  # Read one row
    df = df.sort_values('created')
    df = df.filter(items=['sid', 'gps_breite', 'gps_laenge'])
    df.rename(columns={'gps_laenge': 'trainLongitude', 'gps_breite': 'trainLatitude'}, inplace=True)
    # TODO sort by time


def get_first_image(wikipedia_page):
    htmlcode = wikipedia_page.html()
    try:
        imgcode = re.search('<img.*src=".*".*/>', htmlcode).group(0)
        imagecode_array = imgcode.split()
        for imagecode_part in imagecode_array:
            if "src=" in imagecode_part:
                imagecode_array = imagecode_part.split('"')
                break
        for imagecode_part in imagecode_array:
            if "//" in imagecode_part:
                image_url = "https:" + imagecode_part.split("thumb/")[0] + imagecode_part.split("thumb/")[1].rsplit("/",1)[0]
                return image_url
    except:
        return ''

i = 0
def get_poi(poi):
    poi, rest = poi.split(";lat")
    lat, lon = rest.split(";lon")
    npoi = {}
    urls = []
    npoi['name'] = poi
    info = wikipedia.page(poi)
    npoi['description'] = info.summary
    try:
        cord = info.coordinates
    except:
        cord = [lat,lon]
    npoi['latitude'] = float(cord[0])
    npoi['longitude'] = float(cord[1])
    npoi['imageUrl'] = get_first_image(info)
    urls.append(info.url)
    npoi['linkUrls'] = urls
    print(npoi['name'], cord)
    return npoi

@default.route('/gps/<int:trainid>/<int:time>')
def browse(trainid, time):
    global df
    df_temp = df[df['sid'] == trainid]
    gjson = df_temp.iloc[time].to_dict()

    result = requests.get("http://api.wikunia.de/sights/api.php?lat=" + str(df_temp.iloc[time]['trainLatitude']) + "&lon=" + str(df_temp.iloc[time]['trainLongitude']) + "&rad=0.05&limit=10")
    print( str(df_temp.iloc[time]['trainLatitude']), str(df_temp.iloc[time]['trainLongitude']))
    rJson = json.loads(result.text)
    pois=[]
    print(rJson)

    for _, poi in rJson.items():
        if isinstance(poi, dict):
            print(poi['sight'])
            pois.append(poi['sight']+";lat"+poi['lat']+";lon"+poi['lon'])
    print(len(pois))

    #pois = wikipedia.geosearch(df_temp.iloc[time]['trainLatitude'], df_temp.iloc[time]['trainLongitude'])
    poi_list = []

    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    poi_list = pool.map(get_poi, pois)
    pool.close()
    #for i in pois:
     #   print(i)
      #  poi_list.append(get_poi(i))
    gjson['pois'] = poi_list
    return jsonify(dict(gjson))

