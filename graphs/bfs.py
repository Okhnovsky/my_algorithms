# Вычислительная сложность O(V + E), где V - кол-во вершин, E - кол-во ребер.
# Пространственная сложность O(V), так как создаетс стек и коллекция
# посещенных вершин.


from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)  # Обработка узла

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)


# Пример использования:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}
bfs(graph, 'A')
