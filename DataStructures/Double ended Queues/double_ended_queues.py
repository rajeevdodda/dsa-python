class Dequeue:
    CAPACITY = 4

    def __init__(self):
        self._data = [None] * Dequeue.CAPACITY
        self._dequeue_length = Dequeue.CAPACITY
        self._front = -1
        self._rear = 0
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def first(self):
        if self.is_empty():
            raise DequeueEmptyException
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise DequeueEmptyException
        return self._data[self._rear]

    def add_first(self, x):
        if self._size == self._dequeue_length:
            self._resize(self._dequeue_length * 2)
        if self._front == -1:
            self._front, self._rear = 0, 0
        elif self._front == 0:
            self._front = self._dequeue_length - 1
        else:
            self._front -= 1
        self._data[self._front] = x
        self._size += 1

    def add_last(self, x):
        if self._size == self._dequeue_length:
            self._resize(self._dequeue_length * 2)
        if self._front == -1:
            self._front, self._rear = 0, 0
        elif self._rear == self._dequeue_length - 1:
            self._rear = 0
        else:
            self._rear += 1
        self._data[self._rear] = x
        self._size += 1

    def delete_first(self):
        if self.is_empty():
            raise DequeueEmptyException
        answer = self._data[self._front]
        self._data[self._front] = None
        if self._front == self._dequeue_length:
            self._front = 0
        else:
            self._front += 1
        self._size -= 1
        return answer

    def delete_last(self):
        if self.is_empty():
            raise DequeueEmptyException
        answer = self._data[self._rear]
        self._data[self._rear] = None
        if self._rear == 0:
            self._rear = self._dequeue_length - 1
        else:
            self._rear -= 1
        self._size -= 1
        return answer

    def _resize(self, capacity):
        temp = [None] * capacity
        old_data = self._data
        walk = self._front
        for i in range(self._dequeue_length):
            if walk == self._dequeue_length:
                walk = 0
            temp[i] = old_data[walk]
            walk += 1
        self._data = temp
        self._front = 0
        self._rear = self._dequeue_length - 1
        self._dequeue_length = capacity


class DequeueEmptyException(Exception):
    pass


d = Dequeue()
d.add_first(1)
d.add_first(2)
d.add_first(3)
d.add_first(4)
d.add_first(5)
d.add_last(6)
d.add_last(7)
d.add_last(8)
d.add_last(9)
d.add_last(10)
print(d.first(), d.last())

print(d._data)
