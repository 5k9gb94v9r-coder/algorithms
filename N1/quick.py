def partition(list, start, pivot):
    i = start
    while i < pivot:
        if list[i] > list[pivot] and i == pivot - 1:
            list[i], list[pivot] = list[pivot], list[i]
            pivot -= 1
        elif list[i] > list[pivot]:
            list[pivot - 1], list[pivot] = list[pivot], list[pivot - 1]
            list[i], list[pivot] = list[pivot], list[i]
            pivot -= 1
        else:
            i += 1
    return pivot

def quick_sort(list, start, end):
    if start < end:
        pivot = partition(list, start, end)
        quick_sort(list, start, pivot - 1)
        quick_sort(list, pivot + 1, end)

if __name__ == "__main__":
    list1 = [5, 98, 51, 3, 14]
    print("Исходный массив:", list1)
    quick_sort(list1, 0, len(list1) - 1)
    print("Отсортированный массив:", list1)