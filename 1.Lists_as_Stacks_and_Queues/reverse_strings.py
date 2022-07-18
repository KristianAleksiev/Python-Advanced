start_string = input()

# as stack
s = []
for symbol in start_string:
    s.append(symbol)  # Push

reversed_string = ""

while s:
    reversed_string += s.pop()


print(reversed_string)
