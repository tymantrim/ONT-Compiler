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
        if row[3] == '': #if the row containing their nice thing is empty, then they uploaded a file instead 
            files[row[2]].write("This person uploaded a file, their link is " + row[4])
        else:
            files[row[2]].write(row[3])
        files[row[2]].write('\n\n\n')
    
    for file in files:
        files[file].close()

#For our camp's ONT, the form is structured as such:
#Timestamp,Your Name,Who is this for?,Type your Nice Thing here,OR upload your nice thing as a file
#If your form is different you will need to change the rows
#change row[2] to the row with whoever the nice thing is being sent to
#change row[1] to the row with whoever submitted the nice thing
#change row[3] to the row with the nice thing
#if your form has a place where they can submit a file instead, change row[4] to the row with their file