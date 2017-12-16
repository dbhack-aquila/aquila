import requests
import json


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


if __name__ == "__main__":
    wid = get_wikidata_id("Angela Merkel")
    image_url = get_wikidata_image(wid)
    print(image_url)

