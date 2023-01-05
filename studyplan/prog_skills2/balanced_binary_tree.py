# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def heightdif(self,root,dic):
        h=0
        if(root!=None):
            if(root.left not in dic.keys()):
                dic[root.left]=self.heightdif(root.left,dic)
            if(root.right not in dic.keys()):
                dic[root.right]=self.heightdif(root.right,dic)
            h=1+max(dic[root.left],dic[root.right])
        return h
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        check=True
        dic={}
        if(root!=None):
            self.heightdif(root,dic)
            h=dic[root.left]-dic[root.right]
            if(h==1 or h==0 or h==-1):
                check=self.isBalanced(root.left)
                if(not check):
                    return False
                check=self.isBalanced(root.right)
                if(not check):
                    return False
            else:
                return False
        return check
