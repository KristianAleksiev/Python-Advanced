def sorting_cheeses(**kwargs):
    print(kwargs)
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []
    for name, pieces_count in sorted_cheeses:
        result.append(name)
        result.extend(sorted(pieces_count, reverse=True))

    return "\n".join(str(x) for x in result)


# print(sorting_cheeses(
#     Parmesan=[102, 120, 135],
#     Camembert=[100, 100 ,105, 500, 430],
#     Mozzarella=[50, 125]
# ))
