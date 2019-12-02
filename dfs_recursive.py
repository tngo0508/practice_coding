from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs_helper(self, v, visited):
        visited[v] = True
        print(v, end=' ')
        for x in self.graph[v]:
            if visited[x] == False:
                self.dfs_helper(x, visited)

    def dfs_recursive(self, v):
        visited = [False] * len(self.graph)
        self.dfs_helper(v, visited)

    def dfs_iterative(self, v):
        visited = [False] * len(self.graph)
        stack = []
        stack.append(v)
        while stack:
            s = stack.pop()
            if not visited[s]:
                visited[s] = True
                print(s, end=' ')

            for x in self.graph[s]:
                if not visited[x]:
                    stack.append(x)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.dfs_iterative(2)
