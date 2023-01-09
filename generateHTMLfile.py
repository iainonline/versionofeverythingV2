# Creating an HTML file
# Adding input data to the HTML file
# define the variable

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
        #file.write(f"<html>\n<body>\n<h1>{files}!</h1>\n</body>\n</html>") - works
        objectname = files[:-4]
        file.write(f'<div class="container"><img src="{files}" height="200" width="200" /><p>{objectname}</p></div>')