class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def print_tree(self):
        print(self.value)
        for child in self.children:
            child.print_tree()

# Create the tree
# ...
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# Create the tree
root = TreeNode("F")

# Create the child nodes
node_U = TreeNode("U")
node_N = TreeNode("N")
node_F = TreeNode("F")
node_H = TreeNode("H")
node_G = TreeNode("G")
node_B = TreeNode("B")
node_A = TreeNode("A")
node_I = TreeNode("I")
node_T = TreeNode("T")

# Add the child nodes to their respective parents
root.add_child(node_U)
root.add_child(node_N)
node_N.add_child(node_A)
node_N.add_child(node_I)
node_N.add_child(node_T)
node_U.add_child(node_F)
node_U.add_child(node_H)
node_U.add_child(node_G)
node_H.add_child(node_B)

# Accessing the tree
print(root.value)  # Output: F
print(root.children[0].value)  # Output: U
print(root.children[1].value)  # Output: N
print(root.children[1].children[0].value)  # Output: A
print(root.children[1].children[1].value)  # Output: I
print(root.children[1].children[2].value)  # Output: T
print(root.children[0].children[0].value)  # Output: F
print(root.children[0].children[1].value)  # Output: H
print(root.children[0].children[2].value)  # Output: G
print(root.children[0].children[1].children[0].value)  # Output: B
# Print the tree
root.print_tree()