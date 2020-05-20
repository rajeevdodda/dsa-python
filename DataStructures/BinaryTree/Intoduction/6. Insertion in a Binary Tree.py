from collections import deque


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Tree:
    def __init__(self, data):
        self.root = Node(data)

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.key, end="->")
            self.in_order(root.right)

    def insert(self, key):
        q = deque()
        q.append(self.root)
        while q:
            temp = q.popleft()
            if not temp.left:
                temp.left = Node(key)
                break
            else:
                q.append(temp.left)

            if not temp.right:
                temp.right = Node(key)
                break
            else:
                q.append(temp.right)


tree = Tree(10)
tree.root.left = Node(11)
tree.root.right = Node(9)
tree.root.left.left = Node(7)
tree.root.right.left = Node(15)
tree.root.right.right = Node(8)
tree.in_order(tree.root)
tree.insert(12)
tree.insert(13)
print(" ")
