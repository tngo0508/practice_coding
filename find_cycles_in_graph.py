from collections import defaultdict


def dfs(graph, vertex, visited):
    if vertex in visited:
        return True

    visited[vertex] = True
    print vertex,
    for vertex in graph:
        if dfs(graph[vertex], vertex, visited):
            return True
    return False


def find_cycle(graph):
    visited = defaultdict()

    for vertex in graph.keys():
        if vertex not in visited:
            if dfs(graph[vertex], vertex, visited):
                print vertex
                return True
    return False


graph = {
    'a': {'a2': {}, 'a3': {}},
    'b': {'b2': {}},
    'c': {}
}
print find_cycle(graph)
# False
graph['c'] = graph
print find_cycle(graph)
# True
