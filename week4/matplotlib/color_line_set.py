import matplotlib


import matplotlib.pyplot as plt
import numpy as np

X_1 = range(100)
Y_1 = [value for value in X_1]

X_2 = range(100)
Y_2 = [value + 100 for value in X_2]

plt.plot(X_1,Y_1,color="b",linestyle="dashed", label = 'line_1')
plt.plot(X_2,Y_2,color="r",linestyle="dotted", label = 'line_2')
plt.legend(shadow=True, fancybox=True, loc="lower right")

plt.grid(True, lw = 0.4, ls="--",c=".90")
plt.xlim(-100,200)
plt.ylim(-200,200)

plt.title("Two lines")
plt.show()

