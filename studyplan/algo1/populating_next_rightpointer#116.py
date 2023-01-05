"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def helper(self,root,prev):
        if(root==None):
            return 
        if(prev==None):
            root.next=None
            self.helper(root.left,root.right)
            self.helper(root.right,None)
        else:
            root.next=prev
            self.helper(root.left,root.right)
            self.helper(root.right,root.next.left)

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        prev=None
        self.helper(root,prev)
        return root
