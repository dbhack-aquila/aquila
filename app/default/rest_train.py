import pandas as pd
from . import default
import wikipedia
import json
from flask import jsonify
import re
import os
import multiprocessing
import requests
import urllib


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


def get_first_image_thumbnail(wikipedia_page):
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
                return "https:" + imagecode_part

    except:
        return ''


def get_first_image(thumbnail_url):
    try:
        if thumbnail_url == "":
            return ""
        return thumbnail_url.split("thumb/")[0] + thumbnail_url.split("thumb/")[1].rsplit("/", 1)[0]
    except:
        return ''


def get_wikidata_id(article):
    """Find the Wikidata ID for a given Wikipedia article."""
    query_string = "https://de.wikipedia.org/w/api.php?action=query&prop=pageprops&ppprop=wikibase_item&redirects=1&format=json&titles=" + article

    ret = requests.get(query_string).json()
    id = next(iter(ret["query"]["pages"]))
    return ret["query"]["pages"][id]["pageprops"]["wikibase_item"]

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
    dapp = urllib.parse.urlencode({'action':'wbgetentities','ids':get_wikidata_id(wikidata_id),'languages':'de'})
    query_string = "https://www.wikidata.org/w/api.php?" + dapp
    res = requests.get(query_string).text
    print(query_string)
    item = json.loads(res)

    wdata = item["entities"][wikidata_id]["descriptions"]["de"]["value"]
    return wdata


def get_first_image_2(page):
    wid = get_wikidata_id(page)
    return get_wikidata_image(wid)

def get_poi(poi):
    poi, rest = poi.split(";lat")
    lat, lon = rest.split(";lon")
    npoi = {}
    urls = []
    npoi['name'] = poi
    wid = get_wikidata_id(poi)
    info = wikipedia.page(poi)
    npoi['description'] = info.summary  # get_wikidata_desc(poi)
    npoi['latitude'] = float(lat)
    npoi['longitude'] = float(lon)
    thumbnail_url = get_first_image_thumbnail(info)
    npoi['thumbnailUrl'] = thumbnail_url
    npoi['imageUrl'] = get_first_image(thumbnail_url)  # get_wikidata_image(wid)
    urls.append(info.url)
    npoi['linkUrls'] = urls
    return npoi

@default.route('/gps/<int:trainid>/<int:time>')
def browse(trainid, time):
    global df
    df_temp = df[df['sid'] == trainid]
    gjson = df_temp.iloc[time].to_dict()

    result = requests.get("http://api.wikunia.de/sights/api.php?lat=" + str(df_temp.iloc[time]['trainLatitude']) + "&lon=" + str(df_temp.iloc[time]['trainLongitude']) + "&rad=0.05&limit=10")
    print(str(df_temp.iloc[time]['trainLatitude']), str(df_temp.iloc[time]['trainLongitude']))
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
    #    poi_list.append(get_poi(i))

    gjson['pois'] = poi_list
    return jsonify(dict(gjson))

