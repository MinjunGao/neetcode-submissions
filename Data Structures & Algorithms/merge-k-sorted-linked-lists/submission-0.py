# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        min_heap = []

        dummy = ListNode()
        p = dummy

        for i, head in enumerate(lists):
            if head:
                heapq.heappush(min_heap, (head.val, i, head))
        
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            p.next = node
            p = p.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
        
        return dummy.next