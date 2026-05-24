# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        
        p, q = head, self.flip(slow)
        while p and q:
            p_next = p.next
            p.next = q
            p = q
            q = p_next

    def flip(self, head):
        if not head or not head.next:
            return head
        tail = self.flip(head.next)
        head.next.next = head
        head.next = None
        return tail