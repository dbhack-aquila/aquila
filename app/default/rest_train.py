import pandas as pd
from . import default
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
    df = pd.read_csv(path, sep=';', decimal='.', skiprows=0, nrows=10000)  # Read one row
    df = df.sort_values('created')
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
            image_url = "https:" + imagecode_part.split("thumb/")[0] + imagecode_part.split("thumb/")[1].rsplit("/",1)[0]
            return image_url

def get_wikidata_id(article):
    """Find the Wikidata ID for a given Wikipedia article."""
    query_string = "https://de.wikipedia.org/w/api.php?action=query&prop=pageprops&ppprop=wikibase_item&redirects=1&format=json&titles=%s" % article

    ret_val = requests.get(query_string).text

    pprops = json.loads(ret_val)

    if pprops["query"]["pages"]:
        for _, data in pprops["query"]["pages"].items():
            wikidata_id = data["pageprops"]["wikibase_item"]
            return wikidata_id
    else:
        print("No page returned.")


def get_wikidata_image(wikidata_id):
    """Return the image for the Wikidata item with *wikidata_id*. """
    query_string = "https://www.wikidata.org/wiki/Special:EntityData/%s.json" % wikidata_id
    item = json.loads(requests.get(query_string).text)

    wdata = item["entities"][wikidata_id]["claims"]

    try:
        image_url = "https://commons.wikimedia.org/wiki/File:%s" % wdata["P18"][0]["mainsnak"]["datavalue"]["value"]
    except KeyError:
        print("No image on Wikidata.")
    else:
        return image_url.replace(" ", "_")
        #lat, lon = wdata["P625"][0]["mainsnak"]["datavalue"]["value"]["latitude"], wdata["P625"][0]["mainsnak"]["datavalue"]["value"]["longitude"]

def get_wikidata_desc(wikidata_id):
    """Return the image for the Wikidata item with *wikidata_id*. """
    query_string = "https://www.wikidata.org/w/api.php?action=wbgetentities&ids={}&languages=de".format(wikidata_id)
    item = json.loads(requests.get(query_string).text)

    wdata = item["entities"][wikidata_id]["descriptions"]["de"]["value"]
    return wdata


def get_first_image_2(page):
    wid = get_wikidata_id(page)
    return get_wikidata_image(wid)

def get_poi(poi):
    npoi = {}
    urls = []
    npoi['name'] = poi
    info = wikipedia.page(poi)
    npoi['description'] = get_wikidata_desc(poi)#info.summary
    npoi['latitude'] = float(info.coordinates[0])
    npoi['longitude'] = float(info.coordinates[1])
    npoi['imageUrl'] = get_first_image_2(poi)
    urls.append(info.url)
    npoi['linkUrls'] = urls
    return npoi

@default.route('/gps/<int:trainid>/<int:time>')
def browse(trainid, time):
    global df
    df_temp = df[df['sid'] == trainid]
    gjson = df_temp.iloc[time].to_dict()
    pois = wikipedia.geosearch(df_temp.iloc[time]['trainLatitude'], df_temp.iloc[time]['trainLongitude'])
    poi_list = []

    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    poi_list = pool.map(get_poi, pois)
    pool.close()

    gjson['pois'] = poi_list
    return jsonify(dict(gjson))

