# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        tail = self.reverseList(head)
        dummy = ListNode(-1, tail)
        prev = dummy
        for i in range(1, n):
            prev = prev.next
        prev.next = prev.next.next
        new_tail = dummy.next
        return self.reverseList(new_tail)
    
    def reverseList(self, head):
        if not head or not head.next:
            return head
        tail = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return tail