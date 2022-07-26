"""
Files are stored as sequences of bits
open() returns a file object
io module is the default module for accessing files

Choosing the mode after we open the file
append - "a"
write - "w"
read - "r"
rt - default
rb - binary string - could be used in img processing

Relative pathing:
- Depending on the current position
- ./ means current directory ( current file directory )
- ../ means previous directory

Absolute pathing:
- Path from root

Converting relative path to absolute path:
print(os.path.abspath("./demo.txt"))

Windows pathing:
print(os.sep)
D:\\repos\\python-advanced

Unix based pathing:
/repos/python advanced

Opening a file could lead to an exception - FileNotFoundError, IsADirectoryError, PermissionError

A file is a mutable object
"""
import os
from io import open

file = open("./demo.txt")
print(file.read())

# Open with mode
file2 = open("./demo.txt", "r")

print(os.path.abspath("./demo.txt"))
print(os.sep)

try:
    open("./text.txt", "r")
    print("File found")

except FileNotFoundError:
    print("File not found!")

