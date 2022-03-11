import numpy as np
from pandas import DataFrame, Series


df = DataFrame(np.arange(16).reshape(4,4),columns=list("abcd"))
s = Series(np.arange(10,14), index=list("abcd"))

print(df + s) #column 기준으로 broadcasting 발생

s2 = Series(np.arange(10,14))
print(df+s2)
print(df.add(s2,axis=0)) #axis 기준으로 row broadcasting 실행

