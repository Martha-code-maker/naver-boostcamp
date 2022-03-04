with open("c:\\python_temp\\workspace\\code\\week1\\week2\\File_Handling\\i_have_a_dream.txt", "r") as my_file:
    i = 0
    while True:
        line = my_file.readline()
        if not line:
            break
        print(str(i) + " === " + line.replace("\n",""))
        i  = i+1