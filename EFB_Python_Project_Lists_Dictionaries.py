import os  # this allows interaction with the underlying OS

# this is the current working directory (cwd)
working_directory = os.getcwd() 

# this will list all of the files in that directory
files = os.listdir(working_directory)

# create an empty file and assigns it to the variable 'New_List' where all of the information from the directory will go
New_List = []

for file in files:
    file_path = os.path.realpath(file) # get the path/name of the file
    file_size = os.path.getsize(file) # get the file size
    New_List.append({'path': file_path, 'size:': file_size}) # append the file path/name and size to the list of dictionaries

print (*New_List, sep='\n')  #this prints the key-value pairs on separate lines for ease in reading