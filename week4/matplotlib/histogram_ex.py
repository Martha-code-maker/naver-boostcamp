import matplotlib.pyplot as plt
import numpy as np

X = np.random.rand(1000)
plt.hist(X,bins=100) #data 나누는 개수 100
plt.show()