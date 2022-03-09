import numpy as np


test_array = np.array([1,4,0,2,3,8,9,7],float)
print(test_array>3)
print(test_array[test_array > 3])

condition = test_array<3
print(test_array[condition])