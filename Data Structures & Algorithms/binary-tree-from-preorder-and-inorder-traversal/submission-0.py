# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
    
    def build(self, preorder, pre_start, pre_end, inorder, in_start, in_end):
        if pre_start > pre_end:
            return None
        
        val = preorder[pre_start]
        idx = inorder.index(val)
        root = TreeNode(val)

        root.left = self.build(preorder, pre_start + 1, pre_start + idx - in_start, inorder, in_start, idx - 1)
        root.right = self.build(preorder, pre_start + idx - in_start + 1, pre_end, inorder, idx + 1, in_end)

        return root