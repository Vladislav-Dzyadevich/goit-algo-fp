import heapq

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_heap_tree(heap_array):
    def build_tree_recursively(array, index):
        if index < len(array):
            node = Node(array[index])
            node.left = build_tree_recursively(array, 2 * index + 1)
            node.right = build_tree_recursively(array, 2 * index + 2)
            return node
        return None

    return build_tree_recursively(heap_array, 0)

def draw_tree(root):
    def display(node, level=0):
        if node is not None:
            display(node.right, level + 1)
            print('     ' * level + '->', node.value)
            display(node.left, level + 1)

    display(root)

if __name__ == "__main__":
    heap_array = [1, 3, 5, 7, 9, 2, 4, 34, 2, 1, 2]
    heapq.heapify(heap_array)
    heap_tree_root = build_heap_tree(heap_array)
    draw_tree(heap_tree_root)
