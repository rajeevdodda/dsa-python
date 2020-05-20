class BinaryArray:
    def __init__(self, root, height):
        self.root = root
        self.array = [None] * ((2 ** height) - 1)
        self.array[0] = root

    def add_left(self, key, position):
        if self.array[position]:
            self.array[position * 2 + 1] = key
        else:
            print(" No parent found")

    def add_right(self, key, position):
        if self.array[position]:
            self.array[position * 2 + 2] = key
        else:
            print(" No parent found")


tree = BinaryArray('A', 3)
print(tree.array)
tree.add_right("C", 0)
tree.add_left("D", 1)

tree.add_right("F", 2)
print(tree.array)
