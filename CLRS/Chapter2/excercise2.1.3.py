def linear_search(array, x):
    for i in range(len(array)):
        if array[i] == x:
            return i
    else:
        return None


v = linear_search(list(range(10)), 11)
print(v)

v = linear_search(list(range(10)), 1)
print(v)
