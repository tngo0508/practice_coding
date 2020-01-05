class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def height(tree):
    if tree is None:
        return 0
    return max(height(tree.left), height(tree.right))


def helper(tree):
    if tree is None:
        return 0

    left = helper(tree.left)
    if left == -1:
        return -1

    right = helper(tree.right)
    if right == -1:
        return -1

    if abs(left - right) <= 1:
        return max(left, right) + 1
    return -1


def is_height_balanced(tree):
    return helper(tree) != -1


n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4)
n1 = Node(1, n2, n3)

print(is_height_balanced(n1))
# True
n1 = Node(1, n2)
print(is_height_balanced(n1))
# False
