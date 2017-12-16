import requests
import xml
import urllib.parse
import math
import xml.etree.ElementTree as ET


def get_osm_pois(lat, lon, box_size):

    height = (box_size/(111.13 * math.cos(lat/180 * math.pi)))/2
    width = (box_size/111.13)/2

    lower_lat, upper_lat = lat - height, lat + height
    lower_lon, upper_lon = lon - width, lon + width

    query = urllib.parse.urlencode(
        {"data": 'node["wikidata"]["place"!~".*"](%f,%f,%f,%f);out;'
                 % (lower_lat, lower_lon, upper_lat, upper_lon)
         })

    query_url = "http://overpass-api.de/api/interpreter?" + query

    response = requests.get(query_url).text

    root = ET.fromstring(response)

    pois = []

    for node in root.findall("node"):
        for tag in node.findall("tag"):
            if tag.attrib["k"] == "wikidata":
                pois.append({"latitude": float(node.attrib["lat"]),
                             "longitude": float(node.attrib["lon"]),
                             "wikidata": tag.attrib["v"]})
    return pois
