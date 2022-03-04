import pickle

f = open("c:\\python_temp\\workspace\\code\\week1\\week2\\File_Handling\\list.pickle","wb")
test = [1,2,3,4,5]
pickle.dump(test,f) #stores test object into f
f.close()
