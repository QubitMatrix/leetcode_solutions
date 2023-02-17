# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
globalmin=10**5

class Solution:
    def predecessor(self,root):
        if(root==None):
            return 10**5
        while(root.right!=None):
            root=root.right   
        return root.val
    def successor(self,root):
        if(root==None):
            return 10**5
        while(root.left!=None):
            root=root.left
        return root.val  
    def fun(self,root):
        global globalmin
        if(not root):
            return 10**5
        if(root.left!=None or root.right!=None):
            self.fun(root.left)
            self.fun(root.right)
            pre=self.predecessor(root.left)
            if(pre!=10**5):
                pre=root.val-pre
            suc=self.successor(root.right)
            if(suc!=10**5):
                suc=suc-root.val
            mindif=min(pre,suc)
            globalmin=min(globalmin,mindif)  
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        global globalmin
        self.fun(root)
        dglobal=globalmin
        globalmin=10**5
        return dglobal

