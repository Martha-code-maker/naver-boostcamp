import pickle

class Multiply(object):
    def __init__(self,multiplier):
        self.multiplier = multiplier
    
    def multiply(self, number):
        return number * self.multiplier


f = open("c:\\python_temp\\workspace\\code\\week1\\week2\\File_Handling\\multiply_object.pickle","rb")
multiply_pickle = pickle.load(f)

print(multiply_pickle.multiply(100))