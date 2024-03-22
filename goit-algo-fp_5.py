
import uuid
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(
            node.id, color=node.color, label=node.val
        )  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title="Tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {
        node[0]: node[1]["label"] for node in tree.nodes(data=True)
    }  # Використовуємо значення вузла для міток

    plt.figure(figsize=(10, 7))
    plt.title(title)
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )

    plt.show()


def generate_color(index, total):
    base_color = (90, 90, 255)  # Базовий колір
    intensity_factor = index / total  # Фактор інтенсивності
    new_color = tuple(
        int(base_color[i] + (255 - base_color[i]) * intensity_factor) for i in range(3)
    )
    color = f"#{new_color[0]:02x}{new_color[1]:02x}{new_color[2]:02x}"
    return color


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def bfs_with_colors(root, total):
    if not root:
        return
    visited = []
    queue = deque([(root, 0)])

    while queue:  # Поки черга не порожня, продовжуємо обхід
        node, index = queue.popleft()
        if node.id not in visited:
            node.color = generate_color(index, total)
            visited.append(node.id)

            if node.left:
                queue.append((node.left, index + 2))
            if node.right:
                queue.append((node.right, index + 3))


def dfs_with_colors(node, visited=None, index=0, total=0):
    if visited is None:
        visited = []

    if node and node.id not in visited:
        node.color = generate_color(index, total)
        index += 1
        visited.append(node.id)
        if node.left:
            index = dfs_with_colors(node.left, visited, index, total)
        if node.right:
            index = dfs_with_colors(node.right, visited, index, total)
    return index


if __name__ == "__main__":
    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    root.right.right = Node(2)
    total_nodes = count_nodes(root)

    # Візуалізація обходу в ширину
    bfs_with_colors(root, total_nodes)
    draw_tree(root, "Обхід дерева в ширину")

    # Візуалізація обходу в глибину
    dfs_with_colors(root, total=total_nodes)
    draw_tree(root, "Обхід дерева в глибину")
