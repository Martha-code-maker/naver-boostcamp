import numpy as np


a = np.array([[1,2,3,4,5],[6,7,8,9,10]],int)
print(a)
print(a[:,2:])     #전체 Row의 2열 이상
print(a[1,1:3])    # 1 Row의 1~2열
print(a[1:3])      # 1 Row~ 2Row 전체
