import csv

with open("ont_form.csv", newline='') as form:
    reader = csv.reader(form, quotechar='"')
    for row in reader:
        print(row)