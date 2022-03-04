import pickle

f = open("c:\\python_temp\\workspace\\code\\week1\\week2\\File_Handling\\list.pickle","rb")
test_pickle = pickle.load(f)
print(test_pickle)
f.close()
