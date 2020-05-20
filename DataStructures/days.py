# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(D, S):
    # write your code in Python 3.6
    string_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5}
    return D * string_dict[S]

print(solution(5, "one"))
print(solution(5, "two"))
print(solution(5, "three"))
print(solution(5, "four"))
print(solution(5, "five"))
