class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers_leetcode(self, l1, l2):
        dummy = Node(-1)
        curr = dummy
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum_val = val1 + val2 + carry
            carry = sum_val // 10
            curr.next = Node(sum_val % 10)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry > 0:
            curr.next = Node(carry)
        return dummy.next

    def addTwoNumbers(self, l1, l2):
        a = l1
        b = l2
        carry = 0
        dummy = Node(-1)
        curr = dummy
        while a or b:
            sum_val = a.val + b.val + carry
            carry = sum_val // 10
            curr.next = Node(sum_val % 10)
            curr = curr.next

            if a.next or b.next:
                if not a.next:
                    a.next = Node(0)
                if not b.next:
                    b.next = Node(0)
            elif carry > 0:
                curr.next = Node(carry)

            a = a.next
            b = b.next
        return dummy.next


l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)

l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

ans = Solution().addTwoNumbers(l1, l2)
while ans:
    print(ans.val, end=' ')
    ans = ans.next
