import os

path_value = "/Users/rajeevdodda/PycharmProjects/DSALGO/Algorithms"

print(os.path.getsize(path_value))
# print(os.path.isdir(path))
# print(os.listdir(path))
# print(os.path.join(path, 'timecalculation.py'))


def disk_usage(path_value):
    total = os.path.getsize(path_value)
    if os.path.isdir(path_value):
        for filename in os.listdir(path_value):
            childpath = os.path.join(path_value, filename)
            total += disk_usage(childpath)
    print(total, path_value)
    return total

print(disk_usage(path_value))


