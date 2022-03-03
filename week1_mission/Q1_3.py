num_list = [1,5,7,15,16,22,28,29]


def get_odd_num(num_list):

    i = 0                                    
    while i < len(num_list) :               

        if num_list[i] % 2 == 0 :            
            del num_list[i]                  

        else :                               
            i += 1                           
    
    return num_list


print(get_odd_num(num_list))
     
        