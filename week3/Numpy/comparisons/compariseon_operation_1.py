import numpy as np

test_a = np.array([1,3,0], float)
test_b = np.array([5,2,1], float)

print(test_a > test_b)
print(test_a == test_b)
print((test_a>test_b).any())

