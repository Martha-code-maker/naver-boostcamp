def read_file(file_path):
    with open(file_path, encoding="utf-8") as f:
        lines = f.readlines()
        data = [line.strip().split(',') for line in lines]
    return data
    
file_path = "c:\\python_temp\\workspace\\mission\\week2\\data-01-test-score.csv"
print(read_file(file_path))
