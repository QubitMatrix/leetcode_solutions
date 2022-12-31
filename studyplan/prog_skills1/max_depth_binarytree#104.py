# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        h=0
        if(root!=None):
            l=self.maxDepth(root.left)
            r=self.maxDepth(root.right)
            h=1+max(l,r)
        return h
