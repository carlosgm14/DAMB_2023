import pandas as pd
import os

cwd = os.getcwd()
archivo= cwd +"/medical_data.csv"
print()
print(archivo)
print()
data = pd.read_csv(archivo)

print(data)
print(data.columns)
print(data['age'])
print(data.describe())
print(data.head())
print(data.tail())

clean_data= data.dropna()
print(clean_data)
average_age = clean_data['age'].mean()
print("edad promedio:", average_age)

