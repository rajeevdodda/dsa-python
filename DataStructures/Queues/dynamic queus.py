class Queue:
    DEFAULT_CAPACITY = 2

    def __init__(self):
        self._data = [None] * Queue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        self._queue_length = Queue.DEFAULT_CAPACITY

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise QueueEmptyException
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise QueueEmptyException
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._queue_length
        self._size -= 1
        if 0 < self._size < self._queue_length // 4:
            self._resize(self._queue_length // 2)
        return answer

    def enqueue(self, x):
        if self._size == self._queue_length:
            self._resize(2 * self._queue_length)
        avail = (self._front + self._size) % self._queue_length
        self._data[avail] = x
        self._size += 1

    def _resize(self, capacity):
        old = self._data
        self._data = [None] * capacity
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0
        self._queue_length = capacity


class QueueEmptyException(Exception):
    pass


q = Queue()

q.enqueue(1)
q.enqueue(2)
print(q._data)
print(q.dequeue())
print(q._data)
q.enqueue(4)
print(q._data)
q.enqueue(5)
print(q._data)
