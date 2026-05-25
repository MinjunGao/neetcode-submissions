# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        self.traverse(root)
        return self.res
    
    def traverse(self, root):
        if not root:
            return 0
        left = max(self.traverse(root.left), 0)
        right = max(self.traverse(root.right), 0)
        self.res = max(self.res, left + right + root.val)
        return root.val + max(left, right)
