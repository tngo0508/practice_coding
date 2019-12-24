class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def helper(tree):
    if not tree:
        return -1
    return 1 + max(helper(tree.left), helper(tree.right))


def is_height_balanced(tree):
    if not tree:
        return True
    return abs(helper(tree.left) - helper(tree.right)) < 2 and is_height_balanced(tree.left) and is_height_balanced(tree.right)


    #     1
    #    / \
    #   2   3
    #  /
    # 4
n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4)
n1 = Node(1, n2, n3)

print(is_height_balanced(n1))
# True

#     1
#    /
#   2
#  /
# 4
n1 = Node(1, n2)
print(is_height_balanced(n1))
# False

n4 = Node(4)
n8 = Node(8)
n6 = Node(6)
n7 = Node(7, None, n8)
n5 = Node(5, None, n7)
n2 = Node(2, n4, n5)
n3 = Node(3, None, n6)
n1 = Node(1, n2, n3)
print(is_height_balanced(n1))
# False
