import pandas as pd


df = pd.read_csv('./dataset/cannabis-data.csv')

print(df.head())

print(df.dtypes)

print(df.isnull().sum())
