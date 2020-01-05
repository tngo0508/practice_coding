import collections


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution(object):
    def list_cousins(self, tree, val):
        queue = collections.deque()
        queue.append(tree)
        while queue:
            node = queue.popleft()
            if node.left and node.left.value != val:
                queue.append(node.left)
            if node.right and node.right.value != val:
                queue.append(node.right)
            else:
                break
        return [x.value for x in queue]

        #     1
        #    / \
        #   2   3
        #  / \   \
        # 4   6   5
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(6)
root.right = Node(3)
root.right.right = Node(5)

print(Solution().list_cousins(root, 6))
# [4, 6]
