stack = []
queries_count = int(input())

for _ in range(queries_count):
    query_parts = [int(x) for x in input().split()]
    command = query_parts[0]

    # Add element to the top of the stack
    if command == 1:
        number = query_parts[1]
        stack.append(number)

    # Delete last element
    elif command == 2 and stack:
        stack.pop()

    # Max element
    elif command == 3 and stack:
        print(max(stack))

    # Min element
    elif command == 4 and stack:
        print(min(stack))

reversed_stack = []

while stack:
    reversed_stack.append(stack.pop())

print(*reversed_stack, sep=", ")
