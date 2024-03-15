import matplotlib.pyplot as plt
import random

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
    return root

def inorder_traversal(root, colors):
    if root:
        colors[root.value] = random_color()
        inorder_traversal(root.left, colors)
        print("Visiting node:", root.value, "Color:", colors[root.value])
        inorder_traversal(root.right, colors)

def breadth_first_traversal(root, colors):
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            colors[node.value] = random_color()
            print("Visiting node:", node.value, "Color:", colors[node.value])
            queue.append(node.left)
            queue.append(node.right)

def random_color():
    return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Функція для створення бінарного дерева зі списку значень
def create_binary_tree(values):
    root = None
    for value in values:
        root = insert(root, value)
    return root

# Приклад використання:
values = [5, 3, 8, 1, 4, 7, 9]
tree_root = create_binary_tree(values)

# Для візуалізації збережемо кольори в словнику
colors = {}

# Обходи дерева
print("Inorder Traversal:")
inorder_traversal(tree_root, colors)
print("\nBreadth-first Traversal:")
breadth_first_traversal(tree_root, colors)