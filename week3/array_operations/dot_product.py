import numpy as np

test_a = np.arange(1,7).reshape(2,3)
test_b = np.arange(7,13).reshape(3,2)

print(test_a.dot(test_b))