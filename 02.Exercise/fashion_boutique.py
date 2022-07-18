clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

current_rack_capacity = rack_capacity
racks_counter = 1

while clothes:
    current_clothing = clothes[-1]

    if current_clothing > current_rack_capacity:
        racks_counter += 1
        current_rack_capacity = rack_capacity

    else:
        current_rack_capacity -= current_clothing
        clothes.pop()

print(racks_counter)