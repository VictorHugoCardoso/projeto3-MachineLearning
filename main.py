import pandas as pd

df = pd.read_csv('./diabetes_data.csv')
print(df.head())
print(df.isnull().sum())