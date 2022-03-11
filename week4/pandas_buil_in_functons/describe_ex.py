import pandas as pd
import numpy as np


df = pd.read_csv("c:\\python_temp\\workspace\\code\\week1\\week4\\lambda_map_apply\\wages.csv")
#describe
print(df.describe())

#unique
print(df.race.unique())
print(np.array(dict(enumerate(df["race"].unique()))))

#sum
print(df.sum(axis=0))
print(df.sum(axis=1))

#isnull
print(df.isnull())


#sort_values
#column 값을 기준으로 데이터를 sorting
print(df.sort_values(['age','earn'],ascending=True).head(10))