import json

with open("c:\\python_temp\\workspace\\code\\week1\\week2\\JavaScript_Object_Notation\\json_example.json", "r", encoding="utf8") as f:
    contents = f.read()
    json_data = json.loads(contents)
    print(json_data["emplyees"])


