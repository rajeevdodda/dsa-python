from time import time

start_time = time()
l = []
for i in range(10000):
    l = l + [i]
stop_time = time()

print(stop_time - start_time)


start_time = time()
l = [i for i in range(10000)]
stop_time = time()

print(stop_time - start_time)
