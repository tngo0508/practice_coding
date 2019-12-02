import collections


class Graph:
    def __init__(self):
        self.graph = collections.defaultdict(list)

    def add_edge(self, k, v):
        self.graph[k].append(v)

    def dfs_helper(self, v, visited):
        visited.add(v)
        # visited[v] = True
        print(v, end=' ')
        for neighbor in self.graph[v]:
            # if not visited[neighbor]:
            if neighbor not in visited:
                self.dfs_helper(neighbor, visited)

    def dfs_recursive(self, v):
        # visited = [False] * (len(self.graph) + 1)
        visited = set()
        self.dfs_helper(v, visited)
        # print(visited)


g = Graph()
g.add_edge(1, 4)
g.add_edge(4, 2)
g.add_edge(4, 5)
g.add_edge(4, 1)
g.add_edge(2, 5)
g.add_edge(2, 4)
g.add_edge(5, 3)
g.add_edge(5, 2)
g.add_edge(5, 4)
g.add_edge(3, 3)
print(g.graph)
g.dfs_recursive(2)