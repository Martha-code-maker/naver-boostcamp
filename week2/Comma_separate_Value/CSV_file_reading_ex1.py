line_counter = 0
data_header = []
customer_list = []

with open("c:\\python_temp\\workspace\\code\\week1\\week2\\Comma_separate_Value\\customers.csv") as customer_data:

    while True:
        data = customer_data.readline()
        if not data: break
        if line_counter == 0 :          #first data is data field
            data_header = data.split(",")   # store data filed in data_header list
        else:
            customer_list.append(data.split(','))
        
        line_counter += 1

print("Header : \t", data_header)
for i in range(0,10):               # 10 sample data
    print("Data", i, ": \t\t", customer_list[i])
print(len(customer_list))