import csv

class ReadCSV():
    def __init__(self,file_path):
        self.file_path = file_path
        f = open(file_path,"r")
        reader = csv.reader(f)
        self.content = [list(map(int,scores)) for scores in reader]
        self.sumation = [sum(scores)/ len(scores) for scores in self.content]

    def read_file(self):
        
       return self.content
    

    def merge_list(self):
       return sorted(self.sumation)

file_path = "c:\\python_temp\\workspace\\mission\\week2\\data-01-test-score.csv"
read_csv = ReadCSV(file_path)

print(read_csv.merge_list())