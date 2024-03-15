import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def dijkstra(self, src):
        # Ініціалізація відстаней до всіх вершин як нескінченні
        distances = [float('inf')] * self.vertices
        distances[src] = 0

        # Ініціалізація бінарної купи та додавання початкової вершини
        min_heap = [(0, src)]

        while min_heap:
            # Вибір вершини з найменшою відстанню з бінарної купи
            dist, u = heapq.heappop(min_heap)

            # Перегляд всіх сусідів обраної вершини
            for neighbor, weight in self.graph[u]:
                # Оновлення відстаней до сусідів
                if distances[u] + weight < distances[neighbor]:
                    distances[neighbor] = distances[u] + weight
                    heapq.heappush(min_heap, (distances[neighbor], neighbor))

        return distances

# Приклад використання
if __name__ == "__main__":
    graph = Graph(6)
    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 2, 3)
    graph.add_edge(1, 3, 6)
    graph.add_edge(1, 2, 2)
    graph.add_edge(2, 4, 4)
    graph.add_edge(2, 5, 2)
    graph.add_edge(2, 3, 7)
    graph.add_edge(3, 4, 1)
    graph.add_edge(4, 5, 2)

    src_vertex = 0
    shortest_distances = graph.dijkstra(src_vertex)

    print("Найкоротші відстані від вершини", src_vertex, "до інших вершин:")
    for i in range(len(shortest_distances)):
        print("До вершини", i, ":", shortest_distances[i])
