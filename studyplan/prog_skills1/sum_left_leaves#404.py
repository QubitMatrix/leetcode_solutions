# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,left):
        sum1=0
        if(root!=None):
            if(root.left==None and root.right==None and left==1):
                return root.val
            sum1+=self.helper(root.left,1)
            sum1+=self.helper(root.right,0)
        return sum1
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum_left_leaves=self.helper(root,0)
        return sum_left_leaves
