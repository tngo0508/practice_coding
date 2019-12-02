import collections


class Graph:
    def __init__(self):
        self.graph = collections.defaultdict(list)

    def add_edge(self, k, v):
        self.graph[k].append(v)

    def dfs(self, v):
        stack = []
        stack.append(v)
        visited = set()
        visited.add(v)
        while stack:
            curr_v = stack.pop()
            print(curr_v, end=' ')
            for neighbor in self.graph[curr_v]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)


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
g.dfs(1)
