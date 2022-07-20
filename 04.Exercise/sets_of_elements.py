n, m = [int(x) for x in input().split()]

first = set()
second = set()

for _ in range(n):
    first.add(int(input()))

for _ in range(m):
    second.add(int(input()))

intersection = first.intersection(second)

[print(x) for x in intersection]

# for element in intersection:
#     print(element)