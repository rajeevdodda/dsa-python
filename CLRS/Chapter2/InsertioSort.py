def insertion_sort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i > -1 and key <= array[i]:
            array[i + 1] = array[i]
            i -= 1
        array[i+1] = key
    print(array)


array = [5, 2, 4, 6, 1, 3]
insertion_sort(array)