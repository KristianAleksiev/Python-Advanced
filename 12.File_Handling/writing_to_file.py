"""
Writing modes:
"w" - create file or overwrite file
"a" - create file or append to file
"x" - create a new file or raise exception
"""

file = open("./write_file.txt", "w")
file.write("It works, content overwritten ")


file = open("./write_file.txt", "a")
file.write("Add another line of text to the existing content")

file = open("./write_file.txt", "x")
file.write("The file exists, exception was raised - FileExistsError")



