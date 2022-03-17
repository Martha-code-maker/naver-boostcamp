import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(100,5)
plt.boxplot(data)
plt.show()
