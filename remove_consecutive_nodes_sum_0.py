class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def removeConsecutiveSumTo0(node):
    dummy_head = Node(0, node)
    start = dummy_head
    while start:
        sum = 0
        end = start.next
        while end:
            sum += end.value
            if sum == 0:
                start.next = end.next
                sum = 0
            end = end.next
        start = start.next
    return dummy_head.next


node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node = removeConsecutiveSumTo0(node)
while node:
    print(node.value)
    node = node.next
# 10
