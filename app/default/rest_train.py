import pandas as pd
from . import default


@default.route('/gps/<int:trainid>/<int:time>')
def browse(trainid, time):
    path = "C:\\Users\\PaulBauriegel\\Downloads\\20171212_wifionice\\surveyor_hackathon_data_20171212.csv"
    df = pd.read_csv(path, sep=';', decimal='.', skiprows=0, nrows=100)    # Read one row
    df = df[df['sid'] == trainid]
    df = df.filter(items=['gps_breite', 'gps_laenge'])
    return df.iloc[time].to_json()