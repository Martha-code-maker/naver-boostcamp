import numpy as np

array1 = np.random.rand(5,3)
array2 = np.random.rand(3,2)

dot = array1.dot(array2)
#dot = np.dot(array1, array2)

print(dot,dot.shape)