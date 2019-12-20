import pprint


class Node:
    def __init__(self, isWord, children):
        self.isWord = isWord
        # {a: Node, b: Node}
        self.children = children


class Solution:
    def buildTrie(self, words):
        trie = Node(False, {})
        # construct trie
        for word in words:
            current = trie
            for char in word:
                if char not in current.children:
                    current.children[char] = Node(False, {})
                current = current.children[char]
            current.isWord = True
        return trie

    def autocomplete(self, trie, word):
        current = trie
        for char in word:
            if char not in current.children:
                return []
            current = current.children[char]
        res = []
        self.dfs(current, word, res)
        return res

    def dfs(self, Node, prefix, res):
        if Node.isWord:
            res.append(prefix)
        for char in Node.children:
            current = Node.children[char]
            self.dfs(current, prefix + char, res)


solution = Solution()
trie = solution.buildTrie(['dog', 'door', 'dark', 'cat', 'elephant'])
print(solution.autocomplete(trie, 'do'))

trie = solution.buildTrie(['car', 'cart', 'can', 'cool', 'dog', 'cat', 'elm'])
print(solution.autocomplete(trie, 'ca'))
