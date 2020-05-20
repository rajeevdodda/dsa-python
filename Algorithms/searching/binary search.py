arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def binary_search(arr, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == arr[mid]:
            return True
        elif target > arr[mid]:
            return binary_search(arr, target, mid + 1, high)
        else:
            return binary_search(arr, target, low, mid - 1)


print(binary_search(arr, 10, 0, 8))
print(binary_search(arr, 1, 0, 8))
