import numpy as np


a = np.array([1,2,3])
b = np.array([2,3,4])
print(np.vstack((a,b)))

a = np.array([[1], [2], [3]])
b = np.array([[2], [3], [4]])
print(np.hstack((a,b)))
