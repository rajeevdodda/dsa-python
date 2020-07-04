# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.


def k_average(array, k):
    window_start = 0
    window_end = 0
    ans = 0
    result = list()
    while window_end < len(array):
        ans += array[window_end]
        if window_end >= k - 1:
            result.append(ans / k)
            ans -= array[window_start]
            window_start += 1
        window_end += 1

    print(result)


k_average([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)

k_average([1, 3, 2], 5)
