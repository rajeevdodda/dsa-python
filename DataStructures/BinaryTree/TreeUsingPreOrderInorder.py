class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def build_tree(pre_order: list, in_order: list):
    if not pre_order:
        return None
    node = Node(pre_order[0])
    node_index_in_inorder = in_order.index(node.key)
    node.left = build_tree(pre_order[1:node_index_in_inorder + 1], in_order[:node_index_in_inorder])
    node.right = build_tree(pre_order[node_index_in_inorder + 1:], in_order[node_index_in_inorder + 1:])

    return node


def post_order(root):
    """ Postorder traversal is used to delete the tree. """
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.key, end="->")


t = build_tree(list('abdehicfjgkl'), list('dbheiajfckgl'))

post_order(t)
