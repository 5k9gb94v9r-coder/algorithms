n = int(input("Введите количество элементов: \n"))
a = []

for i in range(n):
    num = int(input(f"Введите элемент {i+1}: \n"))
    a.append(num)

print("Массив:\n", a)

result = []

for i in range(n):
    found = -1
    for j in range(i + 1, n):
        if a[j] < a[i]:
            found = a[j]
            break
    result.append(found)

print("Ближайшие меньшие справа:\n", result)