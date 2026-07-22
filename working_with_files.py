
import os




Bfile = input("Enter the base file you want to copy from: ")
Cfile = input("Enter the copy file you want to copy to: ")

if os.path.exists(Bfile) and os.path.getsize(Bfile) > 0:
    print(f"Base file {Bfile} exists and is not empty.")
    Base = open(Bfile, 'r')
    Base_content = Base.read()
    Base.close()
else:
    print(f"Base file {Bfile} does not exist or is empty.")
    exit()

if os.path.exists(Cfile):
    print(f"Copy file {Cfile} exists.")
    Copy = open(Cfile, 'a')
    copied = Copy.write(f'\n{Base_content}')
    if copied:
      print(f"File {Bfile} has been appended to {Cfile} successfully.")
    
else:
    print(f"Copy file {Cfile} does not exist. Creating a new file.")
    Copy = open(Cfile, 'w')
    copied = Copy.writelines(Base_content)
    if copied:
      print(f"File {Bfile} has been copied to {Cfile} successfully.")

Copy.close()
