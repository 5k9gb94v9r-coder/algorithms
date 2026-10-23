def bubble_sort(list):
    n = len(list)
    while n > 0:
        swapped = False
        for i in range(n - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                swapped = True
        if not swapped:
            break
        n -= 1

if __name__ == "__main__":
    list1 = [5, 98, 51, 3, 14]
    print("Исходный массив:", list1)
    bubble_sort(list1)
    print("Отсортированный массив:", list1)