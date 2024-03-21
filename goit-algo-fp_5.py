import uuid
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
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def dfs_traversal(node, visited=None, step=0):
    if visited is None:
        visited = set()
    
    if node is None:
        return

    visited.add(node)
    node.color = generate_color(step)
    
    print(node.val, end=" ")
    
    dfs_traversal(node.left, visited, step + 1)
    dfs_traversal(node.right, visited, step + 1)

def bfs_traversal(root):
    queue = [(root, 0)]
    visited = set()

    while queue:
        node, step = queue.pop(0)
        if node not in visited:
            visited.add(node)
            node.color = generate_color(step)
            
            print(node.val, end=" ")
            
            if node.left:
                queue.append((node.left, step + 1))
            if node.right:
                queue.append((node.right, step + 1))

def generate_color(step):
    # Генерує колір на основі послідовності кроку обходу
    # Початковий колір: #000000 (чорний)
    hex_color = format(int(16777215 * step / 255), 'x').zfill(6)
    return '#' + hex_color

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Обхід у глибину та візуалізація
print("Depth First Search:")
dfs_traversal(root)
draw_tree(root)

# Скидання кольорів
reset_colors(root)

# Обхід у ширину та візуалізація
print("\nBreadth First Search:")
bfs_traversal(root)
draw_tree(root)