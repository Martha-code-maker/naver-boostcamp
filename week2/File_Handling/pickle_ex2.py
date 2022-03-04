import pickle

class Multiply(object):
    def __init__(self,multiplier):
        self.multiplier = multiplier
    
    def multiply(self, number):
        return number * self.multiplier

muliply = Multiply(5)


f = open("c:\\python_temp\\workspace\\code\\week1\\week2\\File_Handling\\multiply_object.pickle","wb")
pickle.dump(muliply,f)
f.close()
