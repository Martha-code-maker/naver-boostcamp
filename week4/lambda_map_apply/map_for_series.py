import numpy as np
from pandas import Series


s1 = Series(np.arange(10))
print(s1.map(lambda x: x**2).head(5))

z  = {1: 'A', 2: 'B', 3: 'C'}
print(s1.map(z).head(5))

s2 = Series(np.arange(10,20))
print(s1.map(s2).head(5))