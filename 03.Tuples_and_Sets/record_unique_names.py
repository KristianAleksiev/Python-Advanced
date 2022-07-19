#1.
# n = int(input())
#
# names_set = set()
# for _ in range(n):
#     names_set.add(input())
#
# [print(name) for name in names_set]

#2.
n = int(input())
names_set = {input() for _ in range(n)}
[print(name) for name in names_set]

#3.
# [print(name) for name in {input() for _ in range(int(input()))}]
