class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeKthLargestElem(self, head, k):
        p = head
        length = 0
        while p:
            p = p.next
            length += 1
        dummy = Node(-1)
        prev = dummy
        p = head
        for _ in range(length - k):
            prev = p
            p = p.next

        prev.next = p.next
        return head

    def removeKthLargestElem2(self, head, k):
        if not head:
            return None
        dummy = Node(-1)
        dummy.next = head        
        p2 = dummy
        p1 = head
        for _ in range(k):
            p1 = p1.next
        
        while p1:
            p1 = p1.next
            p2 = p2.next
        
        p2.next = p2.next.next
        return dummy.next
        

    def _print(self, head):
        p = head
        while p:
            print(p.val, end=' ')
            p = p.next
            

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

p = Solution().removeKthLargestElem2(head, 5)
Solution()._print(p)