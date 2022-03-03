inputs = "cat32dog16cow"

def find_string(inputs):
    table = str.maketrans("0123456789","          ")
    return inputs.translate(table).split()

string_list = find_string(inputs)
print(string_list)