# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        self.traverse(root, float('-inf'))
        return self.res
    
    def traverse(self, root, limit):
        if not root:
            return
        self.res += 1 if limit <= root.val else 0
        self.traverse(root.left, max(root.val, limit))
        self.traverse(root.right, max(root.val, limit))