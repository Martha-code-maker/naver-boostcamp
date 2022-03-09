import numpy as np

test_array = np.array([1,4,5,"8"],float)
print(test_array.shape)

matrix = [[1,2,5,8],[1,2,5,8],[1,2,5,8]]
print(np.array(matrix,int).shape)

tensor = [[[1,2,5,8],[1,2,5,8],[1,2,5,8]],
          [[1,2,5,8],[1,2,5,8],[1,2,5,8]],
          [[1,2,5,8],[1,2,5,8],[1,2,5,8]],
          [[1,2,5,8],[1,2,5,8],[1,2,5,8]]]
print(np.array(tensor,int).shape)

print(np.array(tensor,int).ndim)
print(np.array(tensor,int).size)