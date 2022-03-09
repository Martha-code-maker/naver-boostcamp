import numpy as np

from week3.Vector.get_norm import l2_norm
import get_norm

def angle(x,y):
    v = np.inner(x,y) / (l2_norm(x) * l2_norm(y))
    theta = np.arccos(v)
    return theta