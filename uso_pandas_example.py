import pandas as pd
import datetime
#import requests
#Iremos viendo diferentes formas de cargar datos en Pytnon(url-csv,API y Archicho local)
#1) Llamada a una web que contiene el archivo CSV
auto = pd.read_csv('http://faculty.marshall.usc.edu/gareth-james/ISL/Auto.csv')

#2)Haciendo uso de un API (ver Notebook)
yesterday = datetime.date.today() - datetime.timedelta(days=1)
print(yesterday);
#api = 'https://earthquake.usgs.gov/fdsnws/event/1/query'

print(auto.head()) # show the first rows of the datasheet
print(auto.tail(3)) #shows the  3 last rows of our datasheet
#print(auto.shape) # shows the size of datasheet (rows,cols)
#print(auto.isnull())# returns true or false acorrding if the cols-rows is null
#print(auto.isnull().sum()) #suma los nulos por columnas
#print(auto.dtypes)
#Uso de DataFrames
df = pd.DataFrame(auto)
print(df.shape)
print(df.describe()) # main Stadistics
print(df.mpg) # magnitude
#data selection
print(df[['mpg','year',]])
print(df[df['weight']>3500])