#!/usr/bin/env python3

# sed -i 's/\r$//' commands.py  
import os
from os import path
import platform

print(os.path.abspath(".")) # To get my current path
print(os.path.basename(os.path.abspath("."))) # To get my current folder name
print(os.path.dirname(os.path.abspath("."))) # To get my parent folder name

path1 ='/mnt/c/Users/zazozo'
path2 = 'Users'

print(path.join(path1,path2)) # To join two paths

# print(help(os.path))

if path.exists(path1):
    
   print(f"Path exists") # To check if a path exists
else:
   print(f"Path does not exist") # To check if a path does not exist

if path.islink(path1):
   print(f"Path is a  link") # To check if a path is a symbolic link
else:
   print(f"Path is not a link") # To check if a path is not a symbolic link

# -----------------------------------------------------------------------------------------------
   

print(os.getcwd()) # To get the current user information
print(os.listdir()) # To get the list of files and directories in the current directory
# os.mkdir('new_folder') # To create a new directory
# os.rmdir('new_folder') # To remove a directory
# os.rename('old_name', 'new_name') # To rename a file or directory
# os.remove('file.txt') # To remove a file


# ------------------------------------------------------------------------------

# system command is used to execute system commands from within Python. For example, you can use `os.system('ls')` to list files in the current directory on Unix-like systems.
# os.system('ls -l') # To execute a system command

# if platform.system() == 'Linux': # To get the name of the operating system
#     print("Running on Linux")
# else:
#     print("Not running on Linux")


# ---------------------------------------------------------------------------------------------
    # walk command is used to generate the file names in a directory tree by walking the tree either top-down or bottom-up. For example, you can use `os.walk('.')` to iterate through all files and directories in the current directory and its subdirectories.
# path = "/mnt/c/Users/zazozo/desktop/React_project"
# # print(list(os.walk(path))) # To walk through the directory tree
# input_path = input("Enter the path to walk through: ")

# for r,d,k  in os.walk(""):
#     for seek in k:
#         if seek== input_path:
#           print(seek) # To print each file and directory in the directory tree


# --------------------------------------------------------------------------

# checking weather a file is a directory or a file

Entered_input = input("Enter the path to check if it is a file or directory: ")

if os.path.isfile(Entered_input):
    print(f"{Entered_input} is a file") # To check if the entered path is a file
elif os.path.isdir(Entered_input):
    print(f"{Entered_input} is a directory") # To check if the entered path is a directory
else:
    print(f"{Entered_input} is neither a file nor a directory") # To check if the entered path is neither a file nor a directory