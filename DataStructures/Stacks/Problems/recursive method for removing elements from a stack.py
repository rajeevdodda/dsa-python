# R-6.4 Give a recursive method for removing all the elements from a stack.


from DataStructures.Stacks.stacks_normal import Stack


class StackRemoveRecursive(Stack):

    def recursive_remove(self):
        if not len(self.stack):
            return
        else:
            self.stack.pop()
            return self.recursive_remove()




sr = StackRemoveRecursive()
for i in range(10):
    sr.push(i)

print(sr.stack)
sr.recursive_remove()
print(sr.stack)
