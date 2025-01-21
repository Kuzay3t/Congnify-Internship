# using pandas to read csv file
import csv
import pandas as pd

def line_break():
    print("*" * 50)

data_list = []
with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)
    for item in data:
        #data_list.append(item)
    #print(data_list)
        print(item)
        
for row in data:
    print(row[1])
        
dataa = pd.read_csv('weather_data.csv')
print(dataa.describe())
line_break()
print(dataa.head())
line_break()
print(dataa.columns)
line_break()
print(dataa.info)
line_break()
print(dataa.isnull().sum())