#!/usr/bin/env python3.7
##Project description: Scenario: Your company needs to learn about the files located on various machines. You have been asked to build a script that extracts information such as the name and size about the files in the current working directory and stores it in a list of dictionaries.

# Import the 'os' module for interacting with the operating system
import os

# Get the current working directory (cwd)
cwd = os.getcwd() 

# List all files and directories in the current working directory
directory_list = os.listdir(cwd) 

# Print the list of files and directories for reference
print(directory_list) 

# Initialize an empty list to store dictionaries containing file information
file_list= []

# Loop through each item in the directory list
for item in directory_list:
    # Get the size of each file using os.path.getsize()
    file_size = os.path.getsize(item)
    
    # Create a dictionary for each file containing its name and size
    file_info = {'Name': item, 'File Size': file_size}
    
    # Append the dictionary to the file_list
    file_list.append(file_info)

# Print the final list of dictionaries containing file information
print(file_list)
    

