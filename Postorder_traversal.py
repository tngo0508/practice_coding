class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return "(" + str(self.value) + ", " + self.left.__repr__() + ", " + self.right.__repr__() + ")"


def helper(order):
    if not order:
        return None
    middle = len(order) // 2
    root = Node(order[middle])
    root.left = helper(order[:middle])
    root.right = helper(order[middle+1:])
    return root


def create_tree(postorder):
    order = sorted(postorder)
    return helper(order)


# 2 is the root node, with 1 as the left child and 3 as the right child
print(create_tree([1, 3, 2]))
print(create_tree([1, 3, 2, 5, 4]))
