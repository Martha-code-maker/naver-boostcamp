import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.,5.,0.2)

plt.plot(t, t**2, 'b^')
plt.plot(t, (1/5)*(t**2), 'gs')
plt.plot(t, (1/15)*(t**2), 'r--')
plt.show()