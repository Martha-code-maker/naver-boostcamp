with open("c:\\python_temp\\workspace\\code\\week1\\week2\\File_Handling\\i_have_a_dream.txt", "r") as my_file:
    content_list = my_file.readlines()
    print(type(content_list))
    print(content_list)