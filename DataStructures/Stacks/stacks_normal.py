class Stack:

    def __init__(self, size=10):
        # initialise am empty stack.
        self.stack = [None] * size
        self.top = -1
        self.size = size

    def __len__(self):
        return self.top + 1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top + 1 == self.size

    def push(self, x):
        if self.is_full():
            raise StackFullException
        else:
            self.top = self.top + 1
            self.stack[self.top] = x

    def pop(self):
        if self.is_empty():
            raise StackEmptyException
        else:
            self.top = self.top - 1
            return self.stack[self.top + 1]

    def top_element(self):
        if self.is_empty():
            raise StackEmptyException
        return self.stack[self.top]

    def stack_size(self):
        return self.top + 1


class StackFullException(Exception):
    pass


class StackEmptyException(Exception):
    pass


# POP PUSH PEEK ech of the three stack operations takes O(1).
