import pandas as pd
import os

path = "C:\\Users\\PaulBauriegel\\Downloads\\20171212_wifionice\\surveyor_hackathon_data_20171212.csv"
df = pd.read_csv(path, sep=';', decimal='.', skiprows=0, nrows=100)    # Read one row
df[['sid','created','gps_breite','gps_laenge']].to_csv('text.csv')