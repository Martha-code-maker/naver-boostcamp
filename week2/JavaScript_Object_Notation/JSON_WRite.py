import json

dict_data = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

with open("c:\\python_temp\\workspace\\code\\week1\\week2\\JavaScript_Object_Notation\\data.json", "w") as f:
    json.dump(dict_data,f)