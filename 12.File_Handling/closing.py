file = open("./demo.txt", "a")
file.close()


with open("./demo.txt", "a") as file:
    text = file.read()
    # Use the file
    # The file is  closed after the code block is executed
