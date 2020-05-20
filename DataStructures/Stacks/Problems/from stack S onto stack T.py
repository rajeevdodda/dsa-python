# R 6.3 Implement a function with signature transfer(S, T) that transfers all elements
# from stack S onto stack T, so that the element that starts at the top
# of S is the first to be inserted onto T, and the element at the bottom of S
# ends up at the top of T.

from DataStructures.Stacks.stacks_normal import Stack


class StackAdvance(Stack):
    def __init__(self):
        super().__init__(size=10)

    def transfer(self, s, t):
        for j in range(len(s)):
            t.push(s.pop())


class StackFullException(Exception):
    pass


class StackEmptyException(Exception):
    pass


s = StackAdvance()
t = StackAdvance()

for i in range(10):
    s.push(i)
s.transfer(s, t)


