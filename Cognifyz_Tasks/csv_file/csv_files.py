# This is used to learn Comma Seperated Values (CSV) files in Python
# CSV files are used to store a large amount of data in a structured format
# CSV files are used to store data in a table format
import csv


def line_break():
    print("*" * 50)

data_list = []
with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)
    for i in data:
        print(i)
        
        
        

#data_list = []
#with open('weather_data.csv') as data_file:
  #  data = data_file.readlines()
   # for i in data:
    #    data_list.append(i.strip())
    #print(data_list)