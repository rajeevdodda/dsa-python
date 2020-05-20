a = [1, 1, 1, 1, 0]
b = [1, 1, 1, 0, 0]


def binary_addition(a, b):
    n = len(a)
    c = [0] * (n + 1)
    temp = 0
    for i in range(len(a) - 1, -1, -1):
        if a[i] + b[i] + temp == 3:
            c[i+ 1] = 1
            temp = 1

        elif a[i] + b[i] + temp == 2:
            temp = 1
            c[i+ 1] = 0
        else:
            temp = 0
            c[i + 1] = a[i] + b[i]
    c[0] = temp
    return c


print(binary_addition(a, b))
