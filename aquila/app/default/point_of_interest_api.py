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
import hashlib


def get_wikidata_id(article):
    """Find the Wikidata ID for a given Wikipedia article."""
    query_string = "https://de.wikipedia.org/w/api.php?action=query&prop=pageprops&ppprop=wikibase_item&redirects=1" \
                   "&format=json&titles=" + article

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


def get_wikipage(article):
    query = "https://de.wikipedia.org/w/api.php?format=json&action=query&prop=extracts|pageprops|info|extracts|pageimages" \
            "&ppprop=wikibase_item&piprop=name&pilimit=20&inprop=url&exintro=&explaintext=&titles="+ article
    ret = requests.get(query).json()
    pid = next(iter(ret["query"]["pages"]))
    dat = ret["query"]["pages"][pid]
    exc = dat["extract"]
    url = dat["fullurl"]
    try:
        img = dat["pageimage"]
        imgmd5 = hashlib.md5(img.encode('utf-8')).hexdigest()
        img_path = "https://upload.wikimedia.org/wikipedia/commons/" + imgmd5[:1] + "/" + imgmd5[:2] + "/" + img
        img_dump = "https://upload.wikimedia.org/wikipedia/commons/thumb/{}/{}/{}/64px-{}"\
            .format(imgmd5[:1], imgmd5[:2], img, img)
    except KeyError:
        img_path = ""
        img_dump = ""
    return [pid,exc,url,img_path, img_dump]

def get_wikidata_desc(wikidata_id):
    """Return the image for the Wikidata item with *wikidata_id*. """
    dapp = urllib.parse.urlencode({'action':'wbgetentities','ids':get_wikidata_id(wikidata_id),'languages':'de'})
    query_string = "https://www.wikidata.org/w/api.php?" + dapp
    res = requests.get(query_string).text
    item = json.loads(res)

    wdata = item["entities"][wikidata_id]["descriptions"]["de"]["value"]
    return wdata


def get_poi(poi):
    poi, rest = poi.split(";lat")
    lat, lon = rest.split(";lon")
    npoi = {}
    urls = []
    npoi['name'] = poi
    pid, exc, url, img_path, img_dump = get_wikipage(poi)
    npoi['description'] = exc
    npoi['latitude'] = float(lat)
    npoi['longitude'] = float(lon)
    npoi['imageUrl'] = img_path
    npoi['thumbnailUrl'] = img_dump
    urls.append(url)
    npoi['linkUrls'] = urls
    return npoi


def get_point_of_interest_json(train_latitude, train_longitude):
    result = requests.get("http://api.wikunia.de/sights/api.php?lat=" + str(train_latitude) + "&lon=" +
                          str(train_longitude) + "&rad=0.05&limit=10")
    r_json = json.loads(result.text)
    pois=[]
    gjson = {'latitude': train_latitude, 'longitude': train_longitude}


    for _, poi in r_json.items():
        if isinstance(poi, dict):
            pois.append(poi['sight']+";lat"+poi['lat']+";lon"+poi['lon'])

    poi_list = []

    # pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    # poi_list = pool.map(get_poi, pois)
    # pool.close()

    for i in pois:
       poi_list.append(get_poi(i))

    gjson['pois'] = poi_list
    return jsonify(dict(gjson))