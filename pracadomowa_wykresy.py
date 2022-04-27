import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl as xl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)
print(df)
#zadanie 1
# grupa = df.groupby('Rok').agg({'Liczba':['sum']})
# print(grupa)
# grupa.plot
# plt.show()
#zadanie 2
# grupa = df.groupby('Plec').agg({'Liczba' : ['sum']})
# print(grupa)
# grupa.plot(kind = 'bar')
# plt.show()
#zadanie 3
# grupa = df.groupby('Plec').agg({'Liczba' : ['sum']})
# a.plot(kind = 'pie', subplots = True,autopct = '%.2f %%' ,fontsize=20 , figsize=(6,6))
# plt.show()

