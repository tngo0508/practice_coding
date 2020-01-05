class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return "(" + str(self.value) + ", " + self.left.__repr__() + ", " + self.right.__repr__() + ")"


def helper(postorder, start, end):
    if start == end:
        return None
    elif end - start == 1:
        return Node(postorder[start])
    root = Node(postorder[end - 1])
    for i in range(start, end):
        if root.value <= postorder[i]:
            root.left = helper(postorder, start, i)
            root.right = helper(postorder, i, end - 1)
            break
    return root


def create_tree(postorder):
    return helper(postorder, 0, len(postorder))


# 2 is the root node, with 1 as the left child and 3 as the right child
print(create_tree([1, 3, 2]))
print(create_tree([1, 3, 2, 5, 4]))
