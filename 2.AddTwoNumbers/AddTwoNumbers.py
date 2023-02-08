# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = cur = ListNode()
        carry = 0
        while l1 or l2:
            d = carry
            if l1 and l2:
                d += l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                d += l1.val
                l1 = l1.next
            elif l2:
                d += l2.val
                l2 = l2.next
            
            cur.next = ListNode(d%10)
            cur = cur.next
            carry = d // 10
        if carry:
            cur.next = ListNode(1)
        return l3.next