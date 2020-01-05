class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def zigzag_order(tree):
    result = []
    currLevel = []
    nextLevel = []
    left_to_right = True
    currLevel.append(tree)

    while 0 < len(currLevel):
        node = currLevel.pop()
        result.append(node.value)
        if left_to_right:
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        else:
            if node.right:
                nextLevel.append(node.right)
            if node.left:
                nextLevel.append(node.left)

        if len(currLevel) == 0:
            left_to_right = not left_to_right
            currLevel, nextLevel = nextLevel, currLevel

    return result


n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n2 = Node(2, n4, n5)
n3 = Node(3, n6, n7)
n1 = Node(1, n2, n3)

print(zigzag_order(n1))
# [1, 3, 2, 4, 5, 6, 7]
