Howdy!
This is the readme/guide for how to use this compilation script for Outside Nice Things!

Step 1:
Download the google sheet containing the form's responses as a .CSV (file -> download -> Comma Seperated Value (.csv))
Download the sheet into this folder and rename it to be "ont_form.csv" (make sure it is exactly like this!!)

Step 2:
Double check to make sure everything is in the correct place and has the correct names
Inside the folder "ONT-Compiler-main" there should be three files
1. ont_compiler.py
2. ont_form.csv
3. README.txt (this file you're reading rn)

Step 3:
Run ont_compiler.py, this can be done a couple ways
1. Opening the file in VSCode or a similar IED and pressing Run
2. Opening your terminal and running the filepath
    For me this is python -u "c:\Users\admin\Documents\ONT Compiler\ont_compiler.py", but will be different depending on where your file is
    Going to the folder and clicking the bar on top of file explorer should highlight the extended file path, copy and paste this to match my example
3. Navigating to this folder (ONT Compiler) in your terminal and running python ont_compiler.py
If you encounter any difficulty in this step feel free to reach out to me

Step 4:
At this point, the program should successfully run and compile the results of the form into a folder name "OutsideNiceThings" containing 26 .rtf 
(Rich Text Files so that they can be opened in Microsoft word or Google Sheets). Each file is made up of blocks of text for each response, the first
line is who submitted this nice thing, and the next line(s) should be either the nice thing submitted, or if they chose to upload a file instead,
a message saying that is what occured and the google drive link to their file submission.
From here, you can choose to copy+paste, change, organize, or stylize the contents of the files to make ONT exactly as you want them!



IN CASE YOU GET AN ERROR:

FileNotFoundError -
This error means the program couldn't find the file containing the form responses
Example error message:
Traceback (most recent call last):
  File "c:\Users\admin\Documents\ONT Compiler\ont_compiler.py", line 7, in <module>
    with open("ont_sheet.csv", newline='') as form:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'ont_sheet.csv'

In this example, the .csv file containing the responses was named "ont_sheet.csv" instead of "ont_form.csv"
Changing the name to ont_form.csv should fix this problem


PermissionError -
This error means that when attempting to create one of the .rtf/word files permission was denied
Example error message:
Traceback (most recent call last):
  File "c:\Users\admin\Documents\ONT Compiler\ont_compiler.py", line 14, in <module>
    files[row[2]] = open('OutsideNiceThings/' + '_'.join(row[2].split()) + '.rtf', 'w', newline='')
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
PermissionError: [Errno 13] Permission denied: 'OutsideNiceThings/Ty_Trimble.rtf'

This error looks a bit more tricky but is actually much simpler, the file is open somewhere on your computer, and
since it is currectly being used (more than likely by Word to view the file), the program isn't allowed to rewrite it
Closing the Word doc or whatever window the file is open in should fix this problem.


Anything else? - 
If you receive an error or crash from the compilation program that is either not one of these, or my
troubleshooting tips didn't work, text or call me and I will look into it.