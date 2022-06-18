#This is a script for removeing all the headers of a csv file
#in the cwd()

from operator import mod
import os,csv

from nbformat import write

os.makedirs(r"C:\Users\HP\Documents\Dev\Pyscripts\csv\headerlesscsv",exist_ok=True)
#loop all the files in the cwd to get all the csv files

for csvFilename in os.listdir(r"C:\Users\HP\Documents\Dev\Pyscripts\csv"):
    if csvFilename.endswith(".csv"):
        break
    print("Removing csv header form --"+csvFilename+"....")
with open(csvFilename) as f:
    row=[]
    readerObj= csv.reader(f)
    for data in readerObj:
        if readerObj.line_num == 1:
            continue
        row.append(data)
with open(os.path.join(r"C:\Users\HP\Documents\Dev\Pyscripts\csv\Headerlesscsv",csvFilename),mode="w",newline="") as nw_File:
    writerObj= csv.writer(nw_File)
    write_data = writerObj.writerow(row)
