import csv
with open("C:\\Users\\HP\\Documents\\Dev\\Pyscripts\\csv\\output.csv",mode="w",newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["spam","egs","beacon","tea"])
    csv_writer.writerow(["cups","morning","grape","coffee"])
    csv_writer.writerow(["table","basin","secret","adi"])
    csv_writer.writerow(["spam!","trim","despite","saint"])