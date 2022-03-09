import numpy as np


a = np.array([[1,2,3],[4.5,5,6]], int)
print(a)
print(a[0,0])
print(a[0][0])

a[0,0]= 12
print(a)
a[0][0]=5
print(a)
