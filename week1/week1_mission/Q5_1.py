from curses.ascii import isdigit


inputs = "cat32dog16cow"

def find_string(inputs: str):
    return "".join([i if not i.isdigit() else " " for i in inputs]).split()

string_list = find_string(inputs)
print(string_list)
