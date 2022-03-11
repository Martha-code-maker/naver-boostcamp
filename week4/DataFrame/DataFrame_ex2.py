from pandas import Series, DataFrame
import pandas as pd
import numpy as np


raw_data = {'first_name': ['Jason',' Molly', 'Tina',' Jake','Amy'],
             'last_name': ['Miller','Jacobson','Ali','Milner','Cooze'],
             'age' :  [42,52,36,24,73],
             'city': ['San Francisco','Baltimore', 'Miami',' Douglas','Boston']}

df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'city','debt'])
df.debt = df.age>40
#print(df.T)
#print(df.values)
#print(df.to_csv())  

del df["debt"]
print(df)