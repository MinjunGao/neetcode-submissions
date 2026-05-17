class Node:

    def __init__(self, total, L, R):
        self.sum = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)
    
    def build(self, nums, L, R):
        if L == R:
            return Node(nums[L], L, R)
        M = (L + R) // 2
        root = Node(0, L, R)
        root.left = self.build(nums, L, M)
        root.right = self.build(nums, M + 1, R)
        root.sum = root.left.sum + root.right.sum
        return root
    
    def update(self, index: int, val: int) -> None:
        self.updateHelper(self.root, index, val)
    
    def updateHelper(self, root, index, val):
        if root.L == root.R:
            root.sum = val
            return
        M = (root.L + root.R) // 2
        if index <= M:
            self.updateHelper(root.left, index, val)
        else:
            self.updateHelper(root.right, index, val)
        root.sum = root.left.sum + root.right.sum
    
    def query(self, L: int, R: int) -> int:
        return self.queryHelper(self.root, L, R)

    def queryHelper(self, root, L, R):
        if R < root.L or root.R < L:
            return 0
        if L <= root.L and root.R <= R:
            return root.sum
        return self.queryHelper(root.left, L, R) + self.queryHelper(root.right, L, R)
