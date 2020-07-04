# find the maximum sum of any contiguous subarray of size ‘k’.
import Patterns.Sliding_Window.Example1


def k_max(array, k):
    ans = float('-inf')
    window_start = 0
    window_length = 0
    slide_total = 0

    for i in range(len(array)):
        slide_total += array[i]

        if window_length == k - 1:
            if slide_total > ans:
                ans = slide_total
            slide_total -= array[window_start]
            window_start += 1
            window_length -= 1
        window_length += 1
    print(ans)


k_max([2, 1, 5, 1, 3, 1], 1)
