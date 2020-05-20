a = [1, 3, 5, 2, 7]


# non increasing
def insertion_sort(arr):
    for j in range(1, len(arr)):
        i = j - 1
        key = arr[j]
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key

    return arr


print(insertion_sort(a))


# non decreasing
def insertion_sort_reverse(arr):
    for j in range(1, len(arr)):
        i = j - 1
        key = arr[j]
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key
    return arr


print(insertion_sort_reverse(a))
