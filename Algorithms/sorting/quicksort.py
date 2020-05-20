def partition(array: list, p, r):
    x = array[r]
    i = p - 1
    j = p
    while j < r:
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
        j += 1
    array[i+1], array[r] = array[r], array[i+1]

    return i + 1


def quick_sort(array: list, p, r):
    if p < r:
        q = partition(array, p, r)
        quick_sort(array, p, q - 1)
        quick_sort(array, q + 1, r)


sample_array = [17, 12, 6, 19, 23, 8, 5, 10]
quick_sort(sample_array, 0, len(sample_array) - 1)
print(sample_array)
