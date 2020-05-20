def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    left_array = [None] * (n1 + 1)
    right_array = [None] * (n2 + 1)

    for i in range(n1):
        left_array[i] = arr[i]

    for i in range(n2):
        right_array[i] = arr[q + i + 1]

    i = j = 0
    for k in range(p, r):
        if left_array[i] is not None and left_array[i] < right_array[j]:
            arr[k] = left_array[i]
            i += 1
        elif right_array is not None:
            arr[k] = right_array[j]
            j += 1
    return arr


arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

