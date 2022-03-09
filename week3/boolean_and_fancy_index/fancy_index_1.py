import numpy as np


a = np.array([2,4,6,8],float)
b = np.array([0,0,1,3,2,1],int)
print(a[b]) # bracket index , b의 배열의 값을 index로 하여 a 값들을 추출
print(a.take(b))  #bracket index와 같은 효과
