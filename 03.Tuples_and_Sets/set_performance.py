import time

l = list(range(1024 * 15))
s = set(l)
result = False
start = time.time()
for value in s:
    result = value in s
end = time.time()

print(f"Set: {end - start} seconds")

result = False
start = time.time()
for value in l:
    result = value in l
end = time.time()

print(f"List: {end - start} seconds")


