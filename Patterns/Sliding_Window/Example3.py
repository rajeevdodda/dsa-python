# smallest contiguous subarray whose sum is greater than or equal to ‘S’.


def smallest_sub_array_greater_sum(array, k):
    window_start = 0
    window_sum = 0
    window_len = float('inf')

    for window_end in range(len(array)):
        window_sum += array[window_end]
        while window_sum >= k:
            window_len = min(window_len, window_end - window_start + 1)
            window_sum -= array[window_start]
            window_start += 1
    print(window_len)


a = [2, 1, 5, 2, 3, 2]
smallest_sub_array_greater_sum(a, 7)
