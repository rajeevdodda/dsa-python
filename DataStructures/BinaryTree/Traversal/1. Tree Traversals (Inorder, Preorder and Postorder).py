class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Tree:
    def __init__(self, data):
        self.root = Node(data)

    def in_order(self, root):
        """In case of binary search trees (BST), Inorder traversal gives nodes in non-decreasing order. """
        if root:
            self.in_order(root.left)
            print(root.key, end="->")
            self.in_order(root.right)

    def post_order(self, root):
        """ Postorder traversal is used to delete the tree. """
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.key, end="->")

    def pre_order(self, root):
        """ Preorder traversal is used to create a copy of the tree. """
        if root:
            print(root.key, end="->")
            self.pre_order(root.left)
            self.pre_order(root.right)


traversal = Tree(1)
traversal.root.left = Node(2)
traversal.root.right = Node(3)
traversal.root.left.left = Node(4)
traversal.root.left.right = Node(5)

print("In order : ", end="")
traversal.in_order(traversal.root)
print("")

print("Pre order : ", end="")
traversal.pre_order(traversal.root)
print("")

print("Post order : ", end="")
traversal.post_order(traversal.root)

tree = Tree('a')
tree.root.left = Node('b')
tree.root.right = Node('c')
tree.root.left.left = Node('d')
tree.root.left.right = Node('e')
tree.root.left.right.left = Node('h')
tree.root.left.right.right = Node('i')
tree.root.right.left = Node('f')
tree.root.right.right = Node('g')
tree.root.right.left.left = Node('j')
tree.root.right.right.left = Node('k')
tree.root.right.right.right = Node('l')
print("")
tree.pre_order(tree.root)
print()
tree.in_order(tree.root)


