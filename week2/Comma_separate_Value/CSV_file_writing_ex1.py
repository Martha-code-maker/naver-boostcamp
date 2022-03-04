line_counter = 0
data_header = []
employee=[]
customer_USA_only_list = []
customer = None

with open("c:\\python_temp\\workspace\\code\\week1\\week2\\Comma_separate_Value\\customers.csv") as customer_data:

    while 1:
        data = customer_data.readline()
        if not data: break
        if line_counter == 0 :          #first data is data field
            data_header = data.split(",")   # store data filed in data_header list
        else:
            customer = data.split(',')
            if customer[10].upper() == "USA":
                customer_USA_only_list.append(customer)
        line_counter += 1
        
print("Header : \t", data_header)
for i in range(0,10):               # 10 sample data
    print("Data", i, ": \t\t", customer_USA_only_list[i])
print(len(customer_USA_only_list))

with open("c:\\python_temp\\workspace\\code\\week1\\week2\\Comma_separate_Value\\customers_USA_only.csv","w") as customer_USA_only_csv:
    for customer in customer_USA_only_list:
        customer_USA_only_csv.write(",".join(customer).strip('\n')+"\n")