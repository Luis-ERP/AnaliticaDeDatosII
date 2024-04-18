import pandas as pd

df = pd.read_csv('ventas_totales.csv')

df.dropna(inplace=True)
df.to_csv('ventas_totales_sin_na.csv')
