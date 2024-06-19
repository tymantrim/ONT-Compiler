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
            files[row[2]] = open('OutsideNiceThings/' + '_'.join(row[2].split()) + '.rtf', 'w', newline='')
        files[row[2]].write(row[1]+'\n')
        if row[3] == '':
            files[row[2]].write("This person uploaded a file, their link is " + row[4])
        else:
            files[row[2]].write(row[3])
        files[row[2]].write('\n\n\n')
    
    for file in files:
        files[file].close()

