import numpy as np

array1 = np.random.uniform(0,1,15).reshape(5,3)
array2 = np.random.uniform(0,1,6).reshape(3,2)

dot = array1.dot(array2)

print(dot,dot.shape)