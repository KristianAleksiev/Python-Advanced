def fill_the_box(height, length, width, *args):
    volume = height * length * width

    cubes_left = 0

    for el in args:
        if el == "Finish":
            break

        if volume >= el:
            volume -= el
        else:
            el -= volume
            cubes_left += el
            volume = 0

    if volume:
        return f"There is free space in the box. You could put {volume} more cubes."
    else:
        return f"No more free space! You have {cubes_left} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
