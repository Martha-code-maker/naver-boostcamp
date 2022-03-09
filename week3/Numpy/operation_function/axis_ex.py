import numpy as np

test_array = np.arange(1,13).reshape(3,4)
print(test_array)
print(test_array.sum(axis=1))
print(test_array.sum(axis=0))

third_order_tensor = np.array([test_array,test_array,test_array])
print(third_order_tensor)

print(third_order_tensor.sum(axis=2))
print(third_order_tensor.sum(axis=1))
print(third_order_tensor.sum(axis=0))
