import re

inputs = "cat32dog16cow"

def find_string(inputs):
    newstring = re.sub(r'[0-9]+', " ", inputs)
    return newstring.strip().split(' ')

print(find_string(inputs))