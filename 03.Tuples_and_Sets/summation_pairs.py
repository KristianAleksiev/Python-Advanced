numbers = [int(x) for x in input().split()]
target_number = int(input())

unique_pairs = set()

iterations = 0

for first_index in range(0, len(numbers)):
    for second_index in range(first_index + 1, len(numbers)):
        first_num = numbers[first_index]
        second_num = numbers[second_index]

        if first_num + second_num == target_number:
            unique_pairs.add((first_num, second_num))
            print(f'{first_num} + {second_num} = {target_number}')

        iterations += 1

print(f'Iterations done: {iterations}')

for pair in unique_pairs:
    print(pair)