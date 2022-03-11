from pandas import Series, DataFrame
import pandas as pd
import numpy as np


raw_data = {'first_name': ['Jason',' Molly', 'Tina',' Jake','Amy'],
             'last_name': ['Miller','Jacobson','Ali','Milner','Cooze'],
             'age' :  [42,52,36,24,73],
             'city': ['San Francisco','Baltimore', 'Miami',' Douglas','Boston']}

df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'city'])
print(df)
print()

print(DataFrame(raw_data, columns= ['age','city']))
print()
print(DataFrame(raw_data, columns = ['first_name','last_name', 'age','city','debt']))
print()
print(df.first_name)
print(df['first_name'])
print()

print(df.loc[1])
print(df["age"].iloc[1:])
print(df["age"].loc[1:])       