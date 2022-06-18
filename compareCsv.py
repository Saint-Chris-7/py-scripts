#this is program for formatting csv file
#delimeter=/n
#linedelimeter=\n\n
import csv
import os
def csvHandle(file):
    file= os.path.basename(file)
    with open(file) as p_file:
        p_file_reader = csv.reader(p_file)
        for rows in p_file_reader:
            if p_file_reader.line_num == 1:
                continue
    with open("newfile.csv",mode="w",newline="") as f:
        f_writer= csv.writer(f)
        f_writer.writerow(rows)
        print("this is complete")

csvHandle(r"C:\Users\HP\Documents\Dev\Pyscripts\csv\output.csv")

