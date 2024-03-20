import matplotlib.pyplot as plt
import random
import networkx as nx

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

# Функція для візуалізації бінарного дерева
def visualize_binary_tree(root, colors):
    G = nx.Graph()
    add_tree_edges(G, root)
    pos = position_tree(G, root)
    nx.draw(G, pos=pos, with_labels=True, node_color=[colors[node] for node in G.nodes()], node_size=2000, font_size=12)
    plt.show()

# Функція для додавання ребер у граф, яке представляє бінарне дерево
def add_tree_edges(G, root):
    if root:
        if root.left:
            G.add_edge(root.value, root.left.value)
            add_tree_edges(G, root.left)
        if root.right:
            G.add_edge(root.value, root.right.value)
            add_tree_edges(G, root.right)

# Функція для визначення позицій вершин у графі
def position_tree(G, root, level=0, pos=None, width=2.5):
    if pos is None:
        pos = {root.value: (0, 0)}
    else:
        pos[root.value] = (pos[root.parent.value][0] + width * (-1) ** level, -level)

    if root.left:
        root.left.parent = root
        position_tree(G, root.left, level + 1, pos, width / 2)
    if root.right:
        root.right.parent = root
        position_tree(G, root.right, level + 1, pos, width / 2)

    return pos

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

# Візуалізація бінарного дерева
visualize_binary_tree(tree_root, colors)
