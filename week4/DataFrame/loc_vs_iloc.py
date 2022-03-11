from pandas import Series, DataFrame
import pandas as pd
import numpy as np

s = pd.Series(np.nan, index = [49,48,47,46,45,1,2,3,4,5])
print(s.loc[:3])
print(s.iloc[:3])