import numpy as np


a = np.array([1,3,0],float)
print(np.logical_and(a>0 , a<3))

b= np.array([True, False, True], bool)
print(np.logical_not(b))

c = np.array([False, True, False],bool)
print(np.logical_or(b,c))
