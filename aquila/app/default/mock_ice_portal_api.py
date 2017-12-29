import os
import pandas as pd
from flask import jsonify

global init, fake_index, fake_coordinates
fake_index = 0
init = False
fake_coordinates = 0

def init_fake_status():
    global fake_coordinates
    path = os.path.abspath("app/default/surveyor_hackathon_data_20171212.csv")
    fake_coordinates = pd.read_csv(path, sep=';', decimal='.', skiprows=0, nrows=100000)
    fake_coordinates = fake_coordinates[fake_coordinates['sid'] == 40117905]
    fake_coordinates = fake_coordinates.sort_values('created')
    fake_coordinates = fake_coordinates.filter(items=['gps_breite', 'gps_laenge'])
    fake_coordinates.rename(columns={'gps_laenge': 'trainLongitude', 'gps_breite': 'trainLatitude'}, inplace=True)



def get_fake_status():
    global init, fake_index, fake_coordinates
    if not init:
        init_fake_status()
        init = True
    json_dictionary = {'connection': 'true', 'servicelevel': 'AVAILABLE_SERVICE', 'speed': 190, 'wagonClass': 'SECOND',
                       'navigationChange': '2017-12-15-23-02-45', 'isDemo': 'true',
                       'latitude': fake_coordinates.iloc[fake_index % len(fake_coordinates)]['trainLatitude'],
                       'longitude': fake_coordinates.iloc[fake_index % len(fake_coordinates)]['trainLongitude']}
    fake_index += 1
    return json_dictionary


def get_fake_trip_info():
    json_dictionary = {
        'tripDate': '2017-12-16',
        'trainType': 'ICE',
        'vzn': '1627',
        'actualPosition': 242061,
        'distanceFromLastStop': 32,
        'totalDistance': 463178,
        'stopInfo': {
            'scheduledNext': '8010136_00',
            'actualNext': '8010136_00',
            'actualLast': '8010101_00',
            'actualLastStarted': '8010101',
            'finalStationName': 'Frankfurt(Main)Hbf',
            'finalStationEvaNr': '8000105_00'
        },
        'stops': [
            {
                'station': {
                    'evaNr': '8011102_00',
                    'name': 'Berlin Gesundbrunnen',
                    'geocoordinates': {
                        'latitude': 52.548963,
                        'longitude': 13.388513
                    }
                },
                'timetable': {
                    'scheduledArrivalTime': 'null',
                    'actualArrivalTime': 'null',
                    'arrivalDelay': '',
                    'scheduledDepartureTime': 1513447560000,
                    'actualDepartureTime': 1513447560000,
                    'departureDelay': ''
                },
                'track': {
                    'scheduled': '7 D - F',
                    'actual': '7 D - F'
                },
                'info': {
                    'status': 0,
                    'passed': 'true',
                    'distance': 0,
                    'distanceFromStart': 0
                },
                'delayReasons': 'null'
            },
            {
                'station': {
                    'evaNr': '8098160_00',
                    'name': 'Berlin Hbf (tief)',
                    'geocoordinates': {
                        'latitude': 52.525592,
                        'longitude': 13.369545
                    }
                },
                'timetable': {
                    'scheduledArrivalTime': 1513447860000,
                    'actualArrivalTime': 1513447860000,
                    'arrivalDelay': '',
                    'scheduledDepartureTime': 1513448880000,
                    'actualDepartureTime': 1513449120000,
                    'departureDelay': '+4'
                },
                'track': {
                    'scheduled': '2 D - F',
                    'actual': '1'
                },
                'info': {
                    'status': 0,
                    'passed': 'true',
                    'distance': 2899,
                    'distanceFromStart': 2899
                },
                'delayReasons': 'null'
            },
            {
                'station': {
                    'evaNr': '8011113_00',
                    'name': 'Berlin Südkreuz',
                    'geocoordinates': {
                        'latitude': 52.475047,
                        'longitude': 13.365319
                    }
                },
                'timetable': {
                    'scheduledArrivalTime': 1513449180000,
                    'actualArrivalTime': 1513449360000,
                    'arrivalDelay': '+3',
                    'scheduledDepartureTime': 1513449300000,
                    'actualDepartureTime': 1513449480000,
                    'departureDelay': '+3'
                },
                'track': {
                    'scheduled': '3 C - F',
                    'actual': '3 C - F'
                },
                'info': {
                    'status': 0,
                    'passed': 'true',
                    'distance': 5629,
                    'distanceFromStart': 8528
                },
                'delayReasons': 'null'
            },
            {
                'station': {
                    'evaNr': '8010050_00',
                    'name': 'Bitterfeld',
                    'geocoordinates': {
                        'latitude': 51.622861,
                        'longitude': 12.31685
                    }
                },
                'timetable': {
                    'scheduledArrivalTime': 1513452060000,
                    'actualArrivalTime': 1513452060000,
                    'arrivalDelay': '',
                    'scheduledDepartureTime': 1513452600000,
                    'actualDepartureTime': 1513452600000,
                    'departureDelay': ''
                },
                'track': {
                    'scheduled': '3',
                    'actual': '3'
                },
                'info': {
                    'status': 0,
                    'passed': 'true',
                    'distance': 118858,
                    'distanceFromStart': 127386
                },
                'delayReasons': 'null'
            },
            {
                'station': {
                    'evaNr': '8010159_00',
                    'name': 'Halle(Saale)Hbf',
                    'geocoordinates': {
                        'latitude': 51.477509,
                        'longitude': 11.987085
                    }
                },
                'timetable': {
                    'scheduledArrivalTime': 1513453800000,
                    'actualArrivalTime': 1513453800000,
                    'arrivalDelay': '',
                    'scheduledDepartureTime': 1513453920000,
                    'actualDepartureTime': 1513453920000,
                    'departureDelay': ''
                },
                'track': {
                    'scheduled': '8',
                    'actual': '8'
                },
                'info': {
                    'status': 0,
                    'passed': 'true',
                    'distance': 27956,
                    'distanceFromStart': 155342
                },
                'delayReasons': 'null'
            },
            {
                'station': {
                    'evaNr': '8010101_00',
                    'name': 'Erfurt Hbf',
                    'geocoordinates': {
                        'latitude': 50.972551,
                        'longitude': 11.038499
                    }
                },
                'timetable': {
                    'scheduledArrivalTime': 1513455900000,
                    'actualArrivalTime': 1513455900000,
                    'arrivalDelay': '',
                    'scheduledDepartureTime': 1513456380000,
                    'actualDepartureTime': 1513456380000,
                    'departureDelay': ''
                },
                'track': {
                    'scheduled': '2',
                    'actual': '2'
                },
                'info': {
                    'status': 0,
                    'passed': 'false',
                    'distance': 86719,
                    'distanceFromStart': 242061
                },
                'delayReasons': 'null'
            },
            {
                'station': {
                    'evaNr': '8010136_00',
                    'name': 'Gotha',
                    'geocoordinates': {
                        'latitude': 50.93907,
                        'longitude': 10.712568
                    }
                },
                'timetable': {
                    'scheduledArrivalTime': 1513457220000,
                    'actualArrivalTime': 1513457280000,
                    'arrivalDelay': '+1',
                    'scheduledDepartureTime': 1513457340000,
                    'actualDepartureTime': 1513457400000,
                    'departureDelay': '+1'
                },
                'track': {
                    'scheduled': '2',
                    'actual': '2'
                },
                'info': {
                    'status': 0,
                    'passed': 'false',
                    'distance': 23138,
                    'distanceFromStart': 265199
                },
                'delayReasons': 'null'
            },
            {
                'station': {
                    'evaNr': '8010097_00',
                    'name': 'Eisenach',
                    'geocoordinates': {
                        'latitude': 50.976922,
                        'longitude': 10.331986
                    }
                },
                'timetable': {
                    'scheduledArrivalTime': 1513458060000,
                    'actualArrivalTime': 1513458120000,
                    'arrivalDelay': '+1',
                    'scheduledDepartureTime': 1513458180000,
                    'actualDepartureTime': 1513458240000,
                    'departureDelay': '+1'
                },
                'track': {
                    'scheduled': '5',
                    'actual': '5'
                },
                'info': {
                    'status': 0,
                    'passed': 'false',
                    'distance': 26994,
                    'distanceFromStart': 292193
                },
                'delayReasons': 'null'
            },
            {
                'station': {
                    'evaNr': '8000020_00',
                    'name': 'Bad Hersfeld',
                    'geocoordinates': {
                        'latitude': 50.869632,
                        'longitude': 9.716182
                    }
                },
                'timetable': {
                    'scheduledArrivalTime': 1513459860000,
                    'actualArrivalTime': 1513459920000,
                    'arrivalDelay': '+1',
                    'scheduledDepartureTime': 1513459980000,
                    'actualDepartureTime': 1513460040000,
                    'departureDelay': '+1'
                },
                'track': {
                    'scheduled': '2',
                    'actual': '2'
                },
                'info': {
                    'status': 0,
                    'passed': 'false',
                    'distance': 44794,
                    'distanceFromStart': 336987
                },
                'delayReasons': 'null'
            },
            {
                'station': {
                    'evaNr': '8000115_00',
                    'name': 'Fulda',
                    'geocoordinates': {
                        'latitude': 50.554723,
                        'longitude': 9.683977
                    }
                },
                'timetable': {
                    'scheduledArrivalTime': 1513461480000,
                    'actualArrivalTime': 1513461600000,
                    'arrivalDelay': '+2',
                    'scheduledDepartureTime': 1513461600000,
                    'actualDepartureTime': 1513461720000,
                    'departureDelay': '+2'
                },
                'track': {
                    'scheduled': '3',
                    'actual': '3'
                },
                'info': {
                    'status': 0,
                    'passed': 'false',
                    'distance': 35100,
                    'distanceFromStart': 372087
                },
                'delayReasons': 'null'
            },
            {
                'station': {
                    'evaNr': '8000150_00',
                    'name': 'Hanau Hbf',
                    'geocoordinates': {
                        'latitude': 50.120953,
                        'longitude': 8.929
                    }
                },
                'timetable': {
                    'scheduledArrivalTime': 1513463880000,
                    'actualArrivalTime': 1513464000000,
                    'arrivalDelay': '+2',
                    'scheduledDepartureTime': 1513464000000,
                    'actualDepartureTime': 1513464120000,
                    'departureDelay': '+2'
                },
                'track': {
                    'scheduled': '6',
                    'actual': '6'
                },
                'info': {
                    'status': 0,
                    'passed': 'false',
                    'distance': 72113,
                    'distanceFromStart': 444200
                },
                'delayReasons': 'null'
            },
            {
                'station': {
                    'evaNr': '8000105_00',
                    'name': 'Frankfurt(Main)Hbf',
                    'geocoordinates': {
                        'latitude': 50.107145,
                        'longitude': 8.663789
                    }
                },
                'timetable': {
                    'scheduledArrivalTime': 1513465080000,
                    'actualArrivalTime': 1513465200000,
                    'arrivalDelay': '+2',
                    'scheduledDepartureTime': 'null',
                    'actualDepartureTime': 'null',
                    'departureDelay': ''
                },
                'track': {
                    'scheduled': '6',
                    'actual': '6'
                },
                'info': {
                    'status': 0,
                    'passed': 'false',
                    'distance': 18978,
                    'distanceFromStart': 463178
                },
                'delayReasons': 'null'
            }
        ],
        'isDemo': 'true'
    }
    return json_dictionary
