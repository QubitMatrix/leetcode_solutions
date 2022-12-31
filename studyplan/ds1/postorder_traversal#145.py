# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self,root,arr):
        if(root!=None):
            self.traversal(root.left,arr)
            self.traversal(root.right,arr)
            arr.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]
        self.traversal(root,arr)
        return arr
