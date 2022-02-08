class Node:

    def __init__(self, data):
        self.data = data
        self.left = None  # Left child
        self.right = None  # Right child


class BinaryTree:

    def __init__(self, root):
        self.root = Node(root)

    def display(self, print_type):
        if print_type == "preorder":
            return self.pre_order_print(self.root, "")
        elif print_type == "inorder":
            return self.in_order_print(self.root, "")
        elif print_type == "postorder":
            return self.post_order_print(self.root, "")
        else:
            return "print_type " + print_type + " not supported"

    def in_order_print(self, node, traversal):
        if node:
            traversal = self.in_order_print(node.left, traversal)
            traversal += (str(node.data) + "-")
            traversal = self.in_order_print(node.right, traversal)
        return traversal

    def pre_order_print(self, node, traversal):
        if node:
            traversal += (str(node.data) + '-')
            traversal = self.pre_order_print(node.left, traversal)
            traversal = self.pre_order_print(node.right, traversal)
        return traversal

    def post_order_print(self, node, traversal):
        if node:
            traversal = self.post_order_print(node.left, traversal)
            traversal = self.post_order_print(node.right, traversal)
            traversal += (str(node.data) + "-")
        return traversal


if __name__ == "__main__":
    #Level 0
    binary_tree = BinaryTree("F")
    #Level 2
    binary_tree.root.left = Node("B")
    binary_tree.root.right = Node("G")
    #Level 3
    binary_tree.root.left.left = Node("A")
    binary_tree.root.left.right = Node("D")

    binary_tree.root.right.right = Node("I")
    #Level 4
    binary_tree.root.left.right.left = Node("C")
    binary_tree.root.left.right.right = Node("E")

    binary_tree.root.right.right.left = Node("H")

    print("Inorder")
    print(binary_tree.display("inorder"))

    print("Preorder")
    print(binary_tree.display("preorder"))

    print("Postorder")
    print(binary_tree.display("postorder"))
