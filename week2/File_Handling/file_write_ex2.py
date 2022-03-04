with open("c:\\python_temp\\workspace\\code\\week1\\week2\\File_Handling\\count_log.txt", "a", encoding = "utf8") as f:
    for i in range(1,11):
        data = "%d line. \n" %i
        f.write(data)
