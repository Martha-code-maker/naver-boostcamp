from pandas import Series, DataFrame
import pandas as pd
import numpy as np

dict_data = {"a":1, "b":2, "c": 3, "d":4, "e":5}
example_obj = Series(dict_data, dtype = np.float32, name = "example_data")
print(example_obj)

print(example_obj["a"])
example_obj["a"] = 3.2
print(example_obj)
print(example_obj.values)
print(example_obj.index)

example_obj.name = "number"
example_obj.index.name = "alphabet"
print(example_obj)