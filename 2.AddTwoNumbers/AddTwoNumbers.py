# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = "", ""
        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next
        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next
        if not num1:
            num1 = "0"
        if not num2:
            num2 = "0"

        sum = int(num1) + int(num2)

        l3 = cur = ListNode()
        for i in reversed(str(sum)):
            cur.next = ListNode(int(i))
            cur = cur.next
        
        return l3.next