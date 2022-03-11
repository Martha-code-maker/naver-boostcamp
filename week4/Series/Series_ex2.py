from pandas import Series, DataFrame
import pandas as pd


list_data = [1,2,3,4,5]
list_name = ["a","b","c","d","e"]
example_obj = Series(data = list_data, index = list_name)
print(example_obj)