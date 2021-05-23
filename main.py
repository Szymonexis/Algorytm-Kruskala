class Node:
    def __init__(self, value=None):
        # self.children = []
        self.left = None
        self.right = None
        self.value = value

    def __repr__(self):
        return self.value


def add_child(given_node: Node, value):
    if value < given_node.value:
        if given_node.left is None:
            given_node.left = Node(value)
            return
        else:
            add_child(given_node.left, value)
    elif value > given_node.value:
        if given_node.right is None:
            given_node.right = Node(value)
            return
        else:
            add_child(given_node.right, value)


def print_tree(root, level=0):
    if root.left is None and root.right is None:
        print(f"{level}: {root.value}")
    else:
        print(f"{level}: {root.value}")
        level += 1
        if root.right is not None:
            print_tree(root.right, level)
        if root.left is not None:
            print_tree(root.left, level)


true_root = Node()
for val in range(11):
    add_child(true_root, val)
print_tree(true_root)
