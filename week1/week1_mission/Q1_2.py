num_list = [1, 5, 7, 15, 16, 22, 28, 29]

def get_odd_num(num_list):
    return [n for n in num_list if n%2==1]

print(get_odd_num(num_list))
