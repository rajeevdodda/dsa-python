from collections import deque


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Tree:
    def __init__(self, data):
        self.root = Node(data)

    def get_root(self):
        return self.root

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.key, end="->")
            self.in_order(root.right)

    def delete_deepest_node(self, delete_node):
        q = deque()
        q.append(self.root)
        while len(q):
            temp = q.popleft()
            if temp is delete_node:
                temp = None
            if temp.left:
                if temp.left is delete_node:
                    temp.left = None
                    return
                else:
                    q.append(temp.left)
            if temp.right:
                if temp.right is delete_node:
                    temp.right = None
                    return
                else:
                    q.append(temp.right)

    def delete(self, key):
        """Delete a node from it by making sure that tree shrinks from the bottom
        (i.e. the deleted node is replaced by bottom most and rightmost node). """
        # if tree is empty
        if self.root is None:
            return None
        # if tree has only one node i.e,. root node
        if self.root.left is None and self.root.right is None:
            if self.root.key == key:
                return None
            else:
                return root
        q = deque()
        q.append(self.root)

        # initialize key_node with None and track the element to be deleted
        key_node = None
        while len(q):
            # temp will also serve to get last node in level order.
            temp = q.popleft()
            if temp.key == key:
                key_node = temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        # if key_node is not None then there is a match in the tree.
        if key_node:
            x = temp.key
            self.delete_deepest_node(temp)
            key_node.key = x


tree = Tree(10)
root = tree.get_root()
root.left = Node(11)
root.left.left = Node(7)
root.left.right = Node(12)
root.right = Node(9)
root.right.left = Node(15)
root.right.left.right = Node(1)
root.right.right = Node(8)
tree.in_order(root)
tree.delete(11)
print(" ")
tree.in_order(root)
