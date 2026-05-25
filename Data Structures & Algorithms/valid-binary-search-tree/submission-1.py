# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        self.path_max = float('-inf')
        self.traverse(root)
        return self.res
    
    def traverse(self, root):
        if not root:
            return
        self.traverse(root.left)
        if root.val <= self.path_max:
            self.res = False
            return
        self.path_max = root.val
        self.traverse(root.right)