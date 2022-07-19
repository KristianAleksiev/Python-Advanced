numbers_string = input()

occurrences_dict = {}

numbers = [float(x) for x in numbers_string.split(" ")]

for number in numbers:
    if number not in occurrences_dict:
        occurrences_dict[number] = 0
    occurrences_dict[number] += 1

for number, count in occurrences_dict.items():
    print(f"{number:.1f} - {count} times")

