# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.traverse(root, 0)
        return self.res
    
    def traverse(self, root, depth):
        if not root:
            return
        depth += 1
        self.res = max(self.res, depth)
        self.traverse(root.left, depth)
        self.traverse(root.right, depth)
        depth -= 1