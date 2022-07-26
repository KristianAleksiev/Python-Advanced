from os import remove
from os.path import exists
from os import listdir


files_and_dirs_names = listdir("./demo.txt")

if exists("./demo.txt"):
    remove("./demo.txt")
    print("File deleted")

else:
    print("File already deleted")


