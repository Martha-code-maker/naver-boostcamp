class ReadCSV():
    def __init__(self,file_path):
        self.file_path = file_path
        self.data = self.read_file

    def read_file(self):
        with open(file_path, encoding="utf-8") as f:
            lines = f.readlines()
            data = [[int(v) for v in line.strip().split(',')] for line in lines]
        return data

    def merge_list(self,):
        return list(map(sum, self.data))

file_path = "c:\\python_temp\\workspace\\mission\\week2\\data-01-test-score.csv"
read_csv = ReadCSV(file_path)
print(read_csv.read_file())
print(read_csv.merge_list())