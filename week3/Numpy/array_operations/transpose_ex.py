import numpy as np


test_a = np.arange(1,7).reshape(2,3)
print(test_a)
print(test_a.transpose())

print(test_a.T)
print(test_a.T.dot(test_a))