# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        looked = set()
        while cur:
            if cur in looked:
                return cur
            looked.add(cur)
            cur = cur.next
        return None