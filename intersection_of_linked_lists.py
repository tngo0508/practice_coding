def length(head):
    if not head:
        return 0
    return 1 + length(head.next)


def intersection(a, b):
    m, n = length(a), length(b)
    curr_a, curr_b = a, b

    if m > n:
        for _ in range(m - n):
            curr_a = curr_a.next
    else:
        for _ in range(n - m):
            curr_b = curr_b.next

    while curr_a != curr_b:
        curr_a = curr_a.next
        curr_b = curr_b.next
    return curr_a


class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

    def prettyPrint(self):
        c = self
        while c:
            print(c.val)
            c = c.next


a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

c = intersection(a, b)
c.prettyPrint()
# 3 4
