import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val, end='')
    inorder(root.right)


class Solution:
    def valuesAtLevel(self, n, root):
        if not root:
            return []
        if n == 1:
            return [root.val]
        return self.valuesAtLevel(n - 1, root.left) + self.valuesAtLevel(n - 1, root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)
inorder(root)
print('\n')
print(Solution().valuesAtLevel(3, root))
