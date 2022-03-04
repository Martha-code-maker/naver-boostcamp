with open("c:\\python_temp\\workspace\\code\\week1\\week2\\File_Handling\\i_have_a_dream.txt", "r") as my_file:
    contents = my_file.read()
    word_list = contents.split(" ")
    line_list = contents.split("\n")

print("Total number of Characters : ", len(contents))
print("Total number of Words : ", len(word_list))
print("Total number of Lines : ", len(line_list))