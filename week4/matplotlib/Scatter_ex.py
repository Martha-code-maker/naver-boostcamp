import matplotlib.pyplot as plt
import numpy as np


data_1 = np.random.rand(512,2)
data_2 = np.random.rand(512,2)

plt.scatter(data_1[:,0],data_1[:,1],c="b",marker="x")
plt.scatter(data_2[:,0],data_2[:,1],c="r",marker="^")

plt.show()

