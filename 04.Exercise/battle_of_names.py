n = int(input())

even = set()
odd = set()

for row in range(1, n + 1):
    name = input()
    name_sum = sum([ord(x) for x in name]) // row

    if name_sum % 2 == 0:
        even.add(name_sum)
    else:
        odd.add(name_sum)

even_sum = sum(even)
odd_sum = sum(odd)

if odd_sum > even_sum:
    result = odd.difference(even)

elif odd_sum < even_sum:
    result = odd.symmetric_difference(even)

else:
    result = even.union(odd)

print(*result, sep=", ")

