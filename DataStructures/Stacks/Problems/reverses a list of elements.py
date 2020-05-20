# R-6.5 Implement a function that reverses a list of elements by pushing them onto
# a stack in one order, and writing them back to the list in reversed order.

from DataStructures.Stacks.stacks_normal import Stack


class StackReverseList(Stack):

    def reverse_list(self, sample_list):
        for i in sample_list:
            self.push(i)
        for i in range(len(sample_list)):
            l[i] = self.pop()


sr = StackReverseList()
l = [i for i in range(10)]

print("Before reversing list l : ", l)

sr.reverse_list(l)
print("After reversing list l : ", l)
