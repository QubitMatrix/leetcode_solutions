# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def infix(self,root,arr):
        if(root!=None):
            minval=self.infix(root.left,arr)
            arr.append(root.val)
            minval=self.infix(root.right,arr)
        
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr=[]
        self.infix(root,arr)
        minval=999999
        for x in range(1,len(arr)):
            if(arr[x]-arr[x-1]<minval):
                minval=arr[x]-arr[x-1]
        return minval
