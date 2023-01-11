# After you create the images using the file [1. Create names images using DALL.E 2 model.py]
# Run this file to create an html file called body.php
# Open body.php in your browser to view the images created

import os

# specify the extension you want to search for
extension = ".png"

# create an empty list to store the filenames
filenames = []

# use a for loop to iterate over the files in the current directory
for file in os.listdir():
    # check if the file has the specified extension
    if file.endswith(extension):
        # if it does, add the filename to the list
        filenames.append(file)

# print the list of filenames
print(filenames)

# open a new file in write mode
with open("body.php", "w") as file:
    # write the HTML with the variable
    for files in filenames:
        objectname = files[:-4]
        file.write(f'<div class="container"><img src="{files}" height="200" width="200" /><p>{objectname}</p></div>')