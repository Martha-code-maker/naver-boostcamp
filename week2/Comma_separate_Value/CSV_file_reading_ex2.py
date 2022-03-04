import csv

header = []
customers = []

with open("c:\\python_temp\\workspace\\code\\week1\\week2\\Comma_separate_Value\\customers.csv") as customer_data:
    reader = csv.reader(customer_data)
    header = next(reader)
    customers = [row for row in reader]

print("Header : \t", header)
for i in range(0,10):               # 10 sample data
    print("Data", i, ": \t\t", customers[i])
print(len(customers))