class LinkedStack:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._next = next
            self._element = element

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, element):
        self._head = self._Node(element, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty
        result = self._head._element
        self._head = self._head._next
        self._size -= 1
        return result


class Empty(Exception):
    pass


l = LinkedStack()
l.push(5)
l.push(10)
l.push(15)
print(l.pop())
print(l.pop())
print(l.pop())
try:
    print(l.pop())
except Empty:
    print("empty")
