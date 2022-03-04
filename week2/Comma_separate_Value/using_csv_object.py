import csv
seoung_nam_data = []
header = []
rownum = 0

with open("c:\\python_temp\\workspace\\code\\week1\\week2\\Comma_separate_Value\\korea_floating_population_data.csv","r",encoding="utf8") as p_file:
    csv_data = csv.reader(p_file)
    for row in csv_data:
        if rownum == 0:
            header = row
        location = row[7]   #행정구역 field data

        if location.find(u'성남시') != -1:
            seoung_nam_data.append(row)
        rownum += 1

with open("c:\\python_temp\\workspace\\code\\week1\\week2\\Comma_separate_Value\\seoung_nam_floating_population_data.csv", "w", encoding = "utf8") as s_p_file:
    writer = csv.writer(s_p_file, delimiter = '\t', quotechar = "'", quoting = csv.QUOTE_ALL )
    writer.writerow(header)
    for row in seoung_nam_data:
        writer.writerow(row)