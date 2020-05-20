class Stack:

    def __init__(self, size=2):
        # initialise am empty stack.
        self.stack = [None] * size
        self.top = -1
        self.size = size

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top + 1 == self.size

    def push(self, x):
        if self.stack_size() == self.size:
            temp_stack = [None] * (self.size * 2)
            for i in range(self.size):
                temp_stack[i] = self.stack[i]
            self.size *= 2
            self.stack = temp_stack

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


class StackEmptyException(Exception):
    pass


# POP PUSH PEEK ech of the three stack operations takes O(1).
# tight strategy add constant length to stack. f(N) = N + c  ==> Total cost of N pushes is n^2/c

s = Stack(4)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.push(8)
s.push(9)
print(s.stack)
print(s.stack_size())
