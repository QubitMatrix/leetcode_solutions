# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1=[]
        stack2=[]
        stack1.append(p)
        stack2.append(q)
        while(stack1 and stack2):
            ele1=stack1.pop()
            ele2=stack2.pop()
            if((ele1==None) ^ (ele2==None)):
                return False
            if(ele1 and ele2 and ele1.val!=ele2.val):
                return False
            if(ele1):
                stack1.append(ele1.right)
                stack1.append(ele1.left)
            if(ele2):
                stack2.append(ele2.right)
                stack2.append(ele2.left)
        if(stack1 or stack2):
            print("1")
            return False
        return True
