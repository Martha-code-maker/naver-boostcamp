from pandas import Series
import pandas as pd


idx = ["HDD", "SSD", "USB", "CLOUOD"]
data = [19, 11, 5, 97]

series =  Series(data , index = idx)


series = series[(series >= 10) & (series <= 20)]
#series = series[series>=10][series<=20]

print(series)
