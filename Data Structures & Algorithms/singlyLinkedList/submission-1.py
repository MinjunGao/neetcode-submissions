class ListNode:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head
        while i <= index:
            curr = curr.next
            if not curr:
                return -1
            i += 1
        return curr.val

    def insertHead(self, val: int) -> None:
        new_head = ListNode(val, self.head.next)
        self.head.next = new_head
        if not new_head.next:
            self.tail = new_head

    def insertTail(self, val: int) -> None:
        new_tail = ListNode(val)
        self.tail.next = new_tail
        self.tail = new_tail

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        prev = curr
        while i <= index:
            prev = curr
            curr = curr.next
            if not curr:
                return False
            i += 1
        if curr == self.tail:
            self.tail = prev
        prev.next = curr.next
        return True

    def getValues(self) -> List[int]:
        vals = []
        curr = self.head.next
        while curr:
            vals.append(curr.val)
            curr = curr.next
        return vals
