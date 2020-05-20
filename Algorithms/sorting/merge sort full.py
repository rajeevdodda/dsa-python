import sys


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    left_array = [0] * (n1 + 1)
    right_array = [0] * (n2 + 1)
    left_array[-1] = right_array[-1] = sys.maxsize

    for i in range(n1):
        left_array[i] = A[p + i]
    for i in range(n2):
        right_array[i] = A[q + i + 1]

    i = j = 0

    for k in range(p, r):
        if left_array[i] < right_array[j]:
            A[k] = left_array[i]
            i += 1
        else:
            A[k] = right_array[j]
            j += 1


def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


A = [1, 3, 5, 7, 2, 4, 6, 8]

merge_sort(A, 0, 7)
print(A)
