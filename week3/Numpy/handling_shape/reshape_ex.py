import numpy as np


test_matrix = [[1,2,3,4],[1,2,5,8]]
print(np.array(test_matrix).shape)

print(np.array(test_matrix).reshape(8,))
print(np.array(test_matrix).reshape(8,).shape)
print(np.array(test_matrix).reshape(-1,2))   #-1: size를 기반으로 row개수 선정
print(np.array(test_matrix).reshape(2,2,2))