# Вычислительная сложность O(V + E), где V - кол-во вершин, E - кол-во ребер.
# Пространственная сложность O(V), так как создаетс стек и коллекция
# посещенных вершин.


def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)  # Обработка узла

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)  # Обработка узла

            for neighbor in reversed(graph[vertex]):  # Обратный порядок для правильного порядка обхода
                if neighbor not in visited:
                    stack.append(neighbor)


# Пример использования:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}
dfs_recursive(graph, 'A')
dfs_iterative(graph, 'A')
