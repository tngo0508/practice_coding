import collections


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def zigzag_order(tree):
    queue = collections.deque()
    queue.append(tree)
    level = 0
    res = []
    while queue:
        for _ in range(2**level):
            if not queue:
                break
            if level % 2 == 0:
                curr = queue.pop()
            else:
                curr = queue.popleft()
            if curr.right:
                queue.append(curr.right)
            if curr.left:
                queue.append(curr.left)
            res.append(curr.value)
        level += 1
    return res


# n4 = Node(4)
# n5 = Node(5)
# n6 = Node(6)
# n7 = Node(7)
# n2 = Node(2, n4, n5)
# n3 = Node(3, n6, n7)
# n1 = Node(1, n2, n3)

# print(zigzag_order(n1))
# # [1, 3, 2, 4, 5, 6, 7]

n4 = Node(4)
n5 = Node(5)
n2 = Node(2, n4, n5)
n3 = Node(3)
n1 = Node(1, n2, n3)

print(zigzag_order(n1))
# [1, 3, 2, 4, 5]
