number_of_elements = int(input())

result = set()

for _ in range(number_of_elements):
    current_set = set(input().split())
    result = result.union(current_set)

for element in result:
    print(element)