def selection_sort(arr):
    for i in range(len(arr)):

        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


def selection_sort_reverse(arr):
    for i in range(len(arr)):

        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


print(selection_sort([1, 3, 5, 2, 7, 1]))
print(selection_sort_reverse([1, 3, 5, 2, 7, 1]))