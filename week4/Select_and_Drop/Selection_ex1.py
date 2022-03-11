from pandas import Series, DataFrame
import pandas as pd
import numpy as np



df = pd.read_excel("c:\\python_temp\\workspace\\code\\week1\\week4\\Select_and_Drop\\data\\excel-comp-data.xlsx")
print(df["account"].head(3))
print(df[["account","street","state"]]).head(3)
print(df[:3])
print(df["account"][:3])
print()

#series selection
account_series = df["account"]
print(account_series[:3])
print(account_series[[0,1,2]])
print(account_series[account_series<250000])
print()

#index 변경
df.index = df["account"]
del df["account"]
print(df.head())

#basic, loc, iloc selection
df[["name","street"]][:2]
df.loc[[2211829,320563],["name","street"]]
df.iloc[:2,:2]

#index 재설정
df.index = list(range(0,15))
df.head()

#Data drop
df.drop(1)
df.drop([0,1,2,3])
df.drop("city", axis=1)