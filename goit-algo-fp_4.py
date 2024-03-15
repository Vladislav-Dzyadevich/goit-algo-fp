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

def add_edges(heap_graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        heap_graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            heap_graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(heap_graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            heap_graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(heap_graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return heap_graph

def draw_heap(heap_root):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_edges(heap, heap_root, pos)

    colors = [node[1]['color'] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Приклад використання
if __name__ == "__main__":
    heap_root = Node(16)
    heap_root.left = Node(14)
    heap_root.right = Node(10)
    heap_root.left.left = Node(8)
    heap_root.left.right = Node(7)
    heap_root.right.left = Node(9)
    heap_root.right.right = Node(3)

    # Відображення бінарної купи
    draw_heap(heap_root)
