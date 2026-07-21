#!/usr/bin/env python3

import os


print(os.getcwd())
# print(list(os.walk(os.getcwd())))
query_path = input("Enter the path to walk through: ")

if os.path.isfile(query_path):
    print('Enter a directory path for querying')
else:
    all_files_dir = os.listdir(query_path)
    if all_files_dir == 0:
        print('This is an empty Directory')
    else:
        ext_type = input('Input a search ext file type such as .py .txt .sh:  ')
        req_file = []
        for query in all_files_dir:
            if query.endswith(ext_type):
                req_file.append(query)
        if len(req_file)==0 :
            print("there is no file with this extension type in the directory")
        else:
            print(f"List of files with {ext_type} extension in the directory: {req_file}")