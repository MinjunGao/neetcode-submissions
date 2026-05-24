"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original_to_clone = {}
        if not head:
            return

        p = head
        while p:
            original_to_clone[p] = Node(p.val)
            p = p.next
        
        p = head
        while p:
            cloned = original_to_clone[p]
            if p.next:
                cloned.next = original_to_clone[p.next]
            if p.random:
                cloned.random = original_to_clone[p.random]
            p = p.next
        
        return original_to_clone[head]