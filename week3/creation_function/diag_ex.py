import numpy as np


matrix = np.arange(9).reshape(3,3)
print(matrix)
print(np.diag(matrix))
print(np.diag(matrix,k=1)) # k : start index

