# length of the longest substring in it with no more than K distinct characters.


def longest_sub_string(string, k):
    hash_map = dict()
    max_length = 0
    window_start = 0
    for window_end in range(len(string)):
        last = string[window_end]
        if last not in hash_map:
            hash_map[last] = 1
        else:
            hash_map[last] += 1

        while len(hash_map) > k:
            first = string[window_start]
            hash_map[first] -= 1
            if hash_map[first] == 0:
                del hash_map[first]
            window_start +=1
        max_length = max(max_length, window_end - window_start + 1)
    print(max_length)


longest_sub_string('araaci', 2)
longest_sub_string("araaci", 1)
longest_sub_string("cbbebi", 3)
longest_sub_string("aaaaaiiiiiiiii", 1)
