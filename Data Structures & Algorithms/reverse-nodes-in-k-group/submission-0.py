# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        a = b = head
        for _ in range(k):
            if not b:
                return head
            b = b.next
        
        new_head = self.reverseN(a, k)
        a.next = self.reverseKGroup(b, k)
        return new_head
    
    def reverseN(self, head, n):
        if not head or not head.next:
            return head
        
        prev, curr, nxt = None, head, head.next
        for _ in range(n):
            curr.next = prev
            prev = curr
            curr = nxt
            if nxt:
                nxt = nxt.next
        head.next = curr
        return prev