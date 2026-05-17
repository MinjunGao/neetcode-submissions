class MinHeap:
    
    def __init__(self):
        self.min_heap = [0]

    def push(self, val: int) -> None:
        self.min_heap.append(val)
        self.perculate_up(len(self.min_heap) - 1)

    def pop(self) -> int:
        if len(self.min_heap) <= 1:
            return -1
        # self.swap(1, len(self.min_heap) - 1)
        # self.min_heap.pop()
        # self.perculate_down(1)
        # return self.min_heap[1]
        if len(self.min_heap) == 2:
            return self.min_heap.pop()
        self.swap(1, len(self.min_heap) - 1)
        res = self.min_heap.pop()
        self.perculate_down(1)
        return res

    def top(self) -> int:
        if len(self.min_heap) <= 1:
            return -1
        return self.min_heap[1]

    def heapify(self, nums: List[int]) -> None:
        self.min_heap = [0] + nums
        for i in reversed(range(1, len(self.min_heap) // 2 + 1)):
            self.perculate_down(i)
        
    def parent(self, root):
        return root // 2
    
    def left(self, root):
        return root * 2
    
    def right(self, root):
        return root * 2 + 1
    
    def swap(self, i, j):
        self.min_heap[i], self.min_heap[j] = self.min_heap[j], self.min_heap[i]
    
    def is_greater(self, i, j):
        return self.min_heap[i] > self.min_heap[j]
    
    def perculate_up(self, root):
        while root > 1 and self.is_greater(self.parent(root), root):
            self.swap(self.parent(root), root)
            root = self.parent(root)
    
    def perculate_down(self, root):
        while self.left(root) < len(self.min_heap):
            target = self.left(root)
            if self.right(root) < len(self.min_heap) and self.is_greater(target, self.right(root)):
                target = self.right(root)
            if self.is_greater(target, root):
                break
            self.swap(root, target)
            root = target