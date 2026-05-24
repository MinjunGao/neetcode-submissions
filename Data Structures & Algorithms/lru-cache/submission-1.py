class Node:

    def __init__(self, key=-1, val=-1, prev=None, next=None):
        self.key, self.val = key, val
        self.prev, self.next = prev, next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add(self, node):
        left, right = self.tail.prev, self.tail
        left.next = right.prev = node
        node.prev, node.next = left, right
    
    def remove(self, node):
        left, right = node.prev, node.next
        left.next, right.prev = right, left
        node.prev = node.next = None

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
