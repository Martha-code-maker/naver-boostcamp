dict_first = {'사과' : 30, '배' : 15, '감' : 10, '포도' : 10}
dict_second = {'사과' : 5, '감' : 25, '배' : 15, '귤' : 25}

from collections import Counter

def merge_dict(dict_first, dict_second) :
 
    return Counter(dict_first)+ Counter(dict_second)                              

print(merge_dict(dict_first,dict_second))             





