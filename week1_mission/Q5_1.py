import re

inputs = "cat32dog16cow5"

def find_string(inputs):
    
    newstring = re.sub(r'[0-9]+',' ', inputs)
    print(newstring)
    return newstring.strip().split(' ')

print(find_string(inputs))
