import numpy as np
import pandas as pd
import openpyxl as xl
#zadanie 1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)
print(df)

#zadanie 2

#a
# print(df[df['Liczba']> 1000])
#b
# print(df[df['Imie']=='PIOTR'])
#c
# print(df[df['Liczba': [sum]]])
#d

#e
# print(df.groupby('Plec').agg({'Liczba': [sum]}))
#f

