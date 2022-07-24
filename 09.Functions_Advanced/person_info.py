def get_info(name, town, age):
    return f"This is {name} from {town} and he is {age} years old"

info = {
    "name": "Pesho",
    "town": "Burgas",
    "age": 18
}

info2 = {
    "name": "Gosho",
    "town": "Plovdiv",
    "age": 48
}


print(get_info(**info))
print(get_info(**info2))