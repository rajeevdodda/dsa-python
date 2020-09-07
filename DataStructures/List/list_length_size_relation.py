import sys

sample_list = list()

for i in range(30):
    a = len(sample_list)
    b = sys.getsizeof(sample_list)
    print('Length: {0:3d};  Size in bytes: {1:4d}'.format(a, b))
    sample_list.append(None)

