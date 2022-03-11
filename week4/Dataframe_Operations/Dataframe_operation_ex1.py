from pandas import Series, DataFrame
import pandas as pd
import numpy as np

df1 = DataFrame(np.arange(9).reshape(3,3), columns= list("abc"))
df2 = DataFrame(np.arange(16).reshape(4,4), columns= list("abcd"))

print(df1+df2)
print(df1.add(df2, fill_value=0))   #add operation은 NaN값을 0으로 변환
