import numpy as np


a = np.arange(10)
print(a)

print(np.any(a>5), np.any(a<0)) #하나라도 조건에 만족하면 true
print(np.all(a>5), np.all(a<10)) #모두가 조건에 만족한다면 true
