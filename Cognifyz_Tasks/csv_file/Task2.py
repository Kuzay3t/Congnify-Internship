import csv
import pandas as pd

with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)
    for item in data:
        print(item)