import json
import requests
from aquila.app.default.mock_ice_portal_api import get_fake_status, get_fake_trip_info


def get_status():
    try:
        json_file = json.loads(requests.get('https://portal.imice.de/api1/rs/status').text)
        json_file['isDemo'] = 'false'
        return json_file
    except (json.JSONDecodeError, requests.ConnectionError):
        print('Demo Mode - ICE Portal not available')
    return get_fake_status()


def get_trip_info():
    try:
        json_file = json.loads(requests.get('https://portal.imice.de/api1/rs/tripInfo').text)
        json_file['isDemo'] = 'false'
        return json_file
    except (json.JSONDecodeError, requests.ConnectionError):
        print('Demo Mode - ICE Portal not available')
    return get_fake_trip_info()

