# Circular Queues


class Queue:
    def __init__(self, size=4):
        self.head = 0
        self.tail = 0
        self.size = size
        self.queue = [None] * self.size
        self.length = 0

    def enqueue(self, x):
        if self.is_full():
            raise QueueFullException
        else:
            self.queue[self.tail] = x
            self.length += 1
            self.tail += 1
            if self.tail == self.size:
                self.tail = 0

    def dequeue(self):
        if self.is_empty():
            raise QueueEmptyException
        else:
            x = self.queue[self.head]
            self.queue[self.head] = None
            self.head += 1
            self.length -= 1
            if self.head == self.size:
                self.head = 0
            return x

    def is_full(self):
        if self.length == self.size:
            return True

    def is_empty(self):
        if self.length == 0:
            return True

    def len_queue(self):
        return self.length


class QueueFullException(Exception):
    pass


class QueueEmptyException(Exception):
    pass


q = Queue()
q.enqueue(1)
print(q.length, q.queue)
q.enqueue(2)
print(q.length, q.queue)
q.enqueue(3)
print(q.length, q.queue)
q.enqueue(4)
print(q.length, q.queue)
try:
    q.enqueue(5)
    print(q.length, q.queue)
except QueueFullException:
    print("Q full")
    pass

print(q.dequeue())
q.enqueue(5)
print(q.length, q.queue)
print(q.dequeue(), q.queue, q.length)

