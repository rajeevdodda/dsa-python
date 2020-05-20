def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    else:
        return None


print(linear_search([1, 2, 3, 4], 5))
print(linear_search([1, 2, 3, 4], 2))
