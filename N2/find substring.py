s = input()
t = input()

result = []
start = 0

while True:
    idx = s.find(t, start)
    if idx == -1:
        break
    result.append(idx)
    start = idx + 1

print(result)