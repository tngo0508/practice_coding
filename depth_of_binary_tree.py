class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return self.val


def deepest(node, depth=0):
    if not node:
        return 0
    return depth + 1 + max(deepest(node.left), deepest(node.right))


#     a
#    / \
#   b   c
#  /
# d
#  \
#   e
root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.left.left.right = Node('e')
root.right = Node('c')

print(deepest(root))
