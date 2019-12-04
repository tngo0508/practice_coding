import collections


class Solution:
    def create_graph(self, words):
        graph = collections.defaultdict(list)
        for word in words:
            last = word[-1]
            for rest in words:
                if last == rest[0] and rest != word:
                    graph[word].append(rest)
        return graph

    def dfs(self, word, graph):
        seen = set()
        return self.dfs_helper(word, graph, seen)

    def dfs_helper(self, word, graph, seen):
        seen.add(word)
        for neighbor in graph[word]:
            print(word, neighbor)
            if neighbor not in seen:
                return self.dfs_helper(neighbor, graph, seen)
            else:
                return True
        return False


# print(Solution().is_circle(['apple', 'eggs', 'snack', 'karat', 'tuna']))
# # True
# print(Solution().is_circle(['apple', 'edge', 'eggs', 'sa']))
# # True
# print(Solution().is_circle(['apple', 'edge', 'eggs']))
# # False
# words = ['apple', 'edge', 'eggs', 'sa']
words = ['apple', 'eggs', 'snack', 'karat', 'tuna']
graph = Solution().create_graph(words)
print(graph)
print(Solution().dfs(words[0], graph))
