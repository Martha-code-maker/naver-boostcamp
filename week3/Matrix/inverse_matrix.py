import numpy as np


X = np.array([[1,-2,3],
             [7,5,0],
             [-2,-1,2]])

print(np.linalg.inv(X))

print(X @ np.linalg.inv(X))
