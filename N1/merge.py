def merge(list, start, end, mid):
    i = start
    j = mid + 1
    k = 0
    merged_list = []

    while i <= mid and j <= end:
        if list[i] <= list[j]:
            merged_list.append(list[i])
            i += 1
        else:
            merged_list.append(list[j])
            j += 1
        k += 1

    while i <= mid:
        merged_list.append(list[i])
        i += 1
        k += 1

    while j <= end:
        merged_list.append(list[j])
        j += 1
        k += 1

    for index in range(k):
        list[start + index] = merged_list[index]

def merge_sort(list, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(list, start, mid)
        merge_sort(list, mid + 1, end)
        merge(list, start, end, mid)

if __name__ == "__main__":
    list1 = [5, 98, 51, 3, 14]
    print("Исходный массив:", list1)
    merge_sort(list1, 0, len(list1) - 1)
    print("Отсортированный массив:", list1)