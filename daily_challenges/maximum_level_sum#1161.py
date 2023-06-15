import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue=deque()
        queue.append((root,1))
        dic=collections.defaultdict(list)
        while(queue):
            popped,level=queue.popleft()
            dic[level].append(popped.val)
            if(popped.left):
                queue.append((popped.left,level+1))
            if(popped.right):
                queue.append((popped.right,level+1))
        return(max(dic,key=lambda x:sum(dic[x])))
