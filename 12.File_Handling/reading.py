# Whole file
file_one = open("./demo.txt", "r").read()
print(file_one)

# Reading by bytes count - Used when the file is enormous
file = open("./demo.txt", "r")

print(file.read(2))
print(file.read(3))
print(file.read(5))

# Reading line by line
file_read = open("./demo.txt", "r")
while True:
    single_line = file_read.readline()
    if not single_line:
        break
    print(single_line)

# Reading the entire document line by line
file_read_lines = open("./demo.txt", "r")
lines_as_list = file_read_lines.readlines()
print(lines_as_list)