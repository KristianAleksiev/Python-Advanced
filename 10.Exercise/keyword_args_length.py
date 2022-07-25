def kwargs_length(**kwargs):
    return len(kwargs)


dict = {"name": "Peter", "age": 29, "city": "Plovdiv"}

print(kwargs_length(**dict))
