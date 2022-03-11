from pandas import Series, DataFrame
import pandas as pd
import numpy as np

s1 = Series(range(1,6), index=list("abced"))
s2 = Series(range(5,11), index = list("bcedef"))

#index 기준으로 연산 수행. 겹치느 index가 없는 경우 NaN으로 반환
print(s1.add(s2))
print(s1+s2)
