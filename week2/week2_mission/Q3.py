def read_file(file_path):
    data_list = []
    file = open(file_path, "r")
    
    while True:
        line = file.readline().rstrip("\n")
        if line:
            line = line.split(',')
            data_list.append(line)
        else:
            break

    return data_list    

file_path = "c:\\python_temp\\workspace\\mission\\week2\\data-01-test-score.csv"
print(read_file(file_path))



    