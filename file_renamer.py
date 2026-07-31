#!/usr/bin/env python3
try:
    
    import pathlib

    file_path = input("Enter the directory to scan through: ")

    def renamer(files_dir):

            rename = pathlib.Path(files_dir).iterdir()

            for file in rename:
                if file.is_file():
                    new_name = file.name.lower().replace(" ", "_")
                    new_path = file.rename(file.parent/new_name)
                    print(f"{file.name} -> {new_name}")
                else:
                    print(f"Skipping folder: {file.name}")

except Exception as e:
    print(f"An error occurred: {e}")