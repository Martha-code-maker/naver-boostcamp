import numpy as np

a = np.array([1,3,0],float)

print(np.where(a>0, 3,2))

a = np.arange(10)
print(np.where(a>5))

a = np.array([1,np.NaN, np.Inf], float)
print(np.isnan(a))
print(np.isfinite(a))


