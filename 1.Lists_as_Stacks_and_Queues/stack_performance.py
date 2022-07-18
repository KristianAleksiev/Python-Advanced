import time

s = []
count = 2 ** 20
result = 0
start = time.time()
for i in range(100):
    s.append(i)
while s:
    result += s.pop()
end = time.time()
print(end - start)


start = time.time()
for i in range(100):
    s.insert(0, i)
while s:
    result += s.pop(0)

end = time.time()
print(end - start)