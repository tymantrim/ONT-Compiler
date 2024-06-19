import csv
import os

files = {}
if not os.path.isdir("OutsideNiceThings"):
    os.mkdir("OutsideNiceThings")
with open("ont_form.csv", newline='') as form:
    reader = csv.reader(form, quotechar='"')
    for row in reader:
        if row[0] == 'Timestamp':
            continue

        if row[2] not in files:
            files[row[2]] = open('OutsideNiceThings/' + '_'.join(row[2].split()) + '.csv', 'w', newline='')
        files[row[2]].write("This is a test\n")
    
    for file in files:
        files[file].close()

