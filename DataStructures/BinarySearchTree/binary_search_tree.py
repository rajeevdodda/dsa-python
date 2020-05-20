class Node:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree:
    def __init__(self, key=None):
        self.root = Node(key)

    def search(self, key):
        temp_node = self.root
        while temp_node is not None and temp_node.key != key:
            if temp_node.key > key:
                temp_node = temp_node.left
            else:
                temp_node = temp_node.right
        if temp_node:
            return temp_node
        else:
            return None

    def insert_key(self, key):
        if self.root.key is None:
            self.root = Node(key)
        else:
            temp_node = self.root
            prev_node = temp_node
            while temp_node is not None:
                prev_node = temp_node
                if temp_node.key < key:
                    temp_node = temp_node.right
                else:
                    temp_node = temp_node.left

            if prev_node.key < key:
                prev_node.right = Node(key)
                prev_node.right.parent = prev_node
            else:
                prev_node.left = Node(key)
                prev_node.left.parent = prev_node

    def pre_order(self, root):
        """ Preorder traversal is used to create a copy of the tree. """
        if root:
            print(root.key, end="->")
            self.pre_order(root.left)
            self.pre_order(root.right)

    def tree_min(self, temp_node=None):
        if temp_node is None:
            temp_node = self.root
        min_node = None
        while temp_node is not None:
            min_node = temp_node
            temp_node = temp_node.left
        return min_node

    def tree_max(self, temp_node=None):
        if temp_node is None:
            temp_node = self.root
        max_node = None
        while temp_node is not None:
            max_node = temp_node
            temp_node = temp_node.right
        return max_node

    def successor(self, key):
        key_node = self.search(key)
        if key_node.right is not None:
            return self.tree_min(key_node.right)
        else:
            parent_node = key_node.parent
            while parent_node is not None and key_node == parent_node.right:
                key_node = parent_node
                parent_node = key_node.parent
            return parent_node

    def predecessor(self, key):
        key_node = self.search(key)
        if key_node.left is not None:
            return self.tree_max(key_node.left)
        else:
            parent_node = key_node.parent
            while parent_node is not None and key_node == parent_node.left:
                key_node = parent_node
                parent_node = key_node.parent
            return parent_node

    def delete(self, key):
        delete_node = self.search(key)
        if delete_node.left is None and delete_node.right is None:
            if delete_node.parent.left == delete_node:
                delete_node.parent.left = None
            else:
                delete_node.parent.right = None
        elif delete_node.left is None or delete_node.right is None:
            if delete_node.right is None:
                if delete_node.parent.left == delete_node:
                    delete_node.parent.left = delete_node.left
                else:
                    delete_node.parent.right = delete_node.left
            else:
                if delete_node.parent.left == delete_node:
                    delete_node.parent.left = delete_node.right
                else:
                    delete_node.parent.right = delete_node.right
        else:
            predecessor_node = self.predecessor(delete_node.key)
            self.delete(predecessor_node.key)
            delete_node.key = predecessor_node.key

    def in_order(self, root):
        """In case of binary search trees (BST), Inorder traversal gives nodes in non-decreasing order. """
        if root:
            self.in_order(root.left)
            print(root.key, end="->")
            self.in_order(root.right)


bst = BinarySearchTree()
bst.insert_key(8)
bst.insert_key(3)
bst.insert_key(6)
bst.insert_key(1)
bst.insert_key(2)
bst.insert_key(4)
bst.insert_key(7)
bst.insert_key(10)
bst.insert_key(14)
bst.insert_key(13)
bst.insert_key(130)

bst.pre_order(bst.root)
print("")

print("max node :", bst.tree_max().key)
print("min node :", bst.tree_min().key)

print("search 130 : ", bst.search(130))
print("search 10 : ", bst.search(100))

print("successor of 3 :", bst.successor(3).key)
print("successor of 6 :", bst.successor(6).key)
print("successor of 8 :", bst.successor(8).key)
print("successor of  130 :", bst.successor(130))
print("successor of 7 :", bst.successor(7).key)
print("predecessor of 6 :", bst.predecessor(6).key)
print("predecessor of 2 :", bst.predecessor(1))
print("predecessor of 6 :", bst.predecessor(6).key)
bst.delete(130)
print(bst.search(130))
bst.pre_order(bst.root)
bst.delete(14)
print()
bst.pre_order(bst.root)
print()
bst.delete(1)
bst.pre_order(bst.root)
bst.delete(8)
print()
bst.pre_order(bst.root)
bst.delete(7)
print()  
bst.in_order(bst.root)
