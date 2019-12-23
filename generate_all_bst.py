class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        result = str(self.value)
        if self.left:
            result = result + str(self.left)
        if self.right:
            result = result + str(self.right)
        return result


def helper(low, high):
    if low == high:
        return [None]
    bsts = []
    for x in range(low, high):
        left = helper(low, x)
        right = helper(x + 1, high)
        for l in left:
            for r in right:
                bsts.append(Node(x, l, r))
    return bsts


def generate_bst(n):
    return helper(1, n + 1)


for tree in generate_bst(3):
    print(tree)

# Pre-order traversals of binary trees from 1 to n.
# 123
# 132
# 213
# 312
# 321

#   1      1      2      3      3
#    \      \    / \    /      /
#     2      3  1   3  1      2
#      \    /           \    /
#       3  2             2  1
