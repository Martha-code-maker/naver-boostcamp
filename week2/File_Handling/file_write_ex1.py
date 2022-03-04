f = open("c:\\python_temp\\workspace\\code\\week1\\week2\\File_Handling\\count_log.txt","w", encoding ="utf8")
for i in range(1,11):
    data = "%d line. \n" %i
    f.write(data)
f.close()
