class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


def traverse(Node):
    if not Node:
        return
    print(Node.val, end=' ')
    traverse(Node.left)
    traverse(Node.right)


def traverseIterative(Node):
    stack = [Node]
    while stack:
        x = stack.pop()
        print(x, end=' ')
        if x.right:
            stack.append(x.right)
        if x.left:
            stack.append(x.left)



def findNode(p, q, Node):
    if p == Node:
        return q
    if p.left and q.left:
        found = findNode(p.left, q.left, Node)
        if found:
            return found
    if p.right and q.right:
        found = findNode(p.right, q.right, Node)
        if found:
            return found
    return None


def findNode2(p, q, Node):
    stack = [(p, q)]
    while stack:
        (p, q) = stack.pop()
        if p == Node:
            return p
        if p.left and q.left:
            stack.append((p.left, q.left))
        if p.right and q.right:
            stack.append((p.right, q.right))
    return None


p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
p.right.left = TreeNode(4)
p.right.right = TreeNode(5)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)
q.right.left = TreeNode(4)
q.right.right = TreeNode(5)


# traverse(p)
# print('\n')
# traverse(q)

traverseIterative(p)
print('\n')
traverseIterative(q)

# print(findNode(p, q, p.right.left))
# print(findNode2(p, q, p.right.left))
