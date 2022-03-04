class ReadCSV():
    def __init__(self, file_path):
        self.file_path = file_path
        self.data_list = []

    def read_file(self):
        with open(self.file_path) as data:
            while(True):
                line = data.readline()
                if not line: break
                self.data_list.append(line.strip().split(','))
        return self.data_list

read_csv = ReadCSV("c:\\python_temp\\workspace\\mission\\week2\\data-01-test-score.csv")
print(read_csv.read_file())

        
