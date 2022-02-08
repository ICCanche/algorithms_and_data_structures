class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # Left child
        self.right = None  # Right child


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)


if __name__ == "__main__":
    binary_tree = BinaryTree(10)
    binary_tree.root.left = Node(2)
    binary_tree.root.right = Node(12)
    print(binary_tree.root.data)
    print(binary_tree.root.left.data)
    print(binary_tree.root.right.data)
