import numpy as np

test_array = np.arange(1,13).reshape(3,4)
print(test_array)

print(test_array.mean(),test_array.mean(axis=0))
print(test_array.std(), test_array.std(axis=0))

