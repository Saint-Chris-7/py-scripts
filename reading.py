import csv
with open(r"C:\Users\HP\Documents\Dev\Pyscripts\csv\example.csv") as file:
    readerObj= csv.reader(file)    
    for row in readerObj:
        print("Row #"+str(readerObj.line_num)+""+str(row))