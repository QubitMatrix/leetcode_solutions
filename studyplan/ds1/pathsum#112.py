# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,arr,targetSum):
        ans=False
        if(root!=None):
            arr.append(root)
            ans1=self.helper(root.left,arr,targetSum)
            ans2=self.helper(root.right,arr,targetSum)
            ans=ans1 or ans2
            if(sum([x.val for x in arr])==targetSum and arr[-1].left==None and arr[-1].right==None):
                return True
            else:
                arr.pop()
                return False
        return ans

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        arr=[]
        x=self.helper(root,arr,targetSum)
        return x
