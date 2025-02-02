import heapq

class Graph:
    def __init__(self):
        """Ініціалізація графа у вигляді списку суміжності"""
        self.graph = {}

    def add_edge(self, u, v, weight):
        """Додає ребро між вершинами u і v з вагою weight"""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Якщо граф орієнтований, цю стрічку прибрати

    def dijkstra(self, start):
        """Алгоритм Дейкстри для знаходження найкоротших шляхів"""
        min_heap = [(0, start)]  # Куча з (відстань, вершина)
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0

        while min_heap:
            current_distance, current_vertex = heapq.heappop(min_heap)

            # Якщо поточна відстань більша за записану, пропускаємо
            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                # Якщо знайшли коротший шлях
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))

        return distances

# -------------------------- Тестування --------------------------
if __name__ == "__main__":
    graph = Graph()
    
    # Додаємо вершини та ребра
    graph.add_edge('A', 'B', 4)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'C', 5)
    graph.add_edge('B', 'D', 10)
    graph.add_edge('C', 'D', 3)
    graph.add_edge('D', 'E', 8)
    graph.add_edge('E', 'A', 7)

    start_vertex = 'A'
    shortest_paths = graph.dijkstra(start_vertex)

    print(f"Найкоротші шляхи від вершини {start_vertex}:")
    for vertex, distance in shortest_paths.items():
        print(f"До {vertex}: {distance}")
