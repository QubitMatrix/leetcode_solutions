# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root):
            return []
        queue=[(root,0)]
        arr=defaultdict(list)
        while(queue):
            popped_node,popped_level=queue[0]
            queue=queue[1:]
            popped_ele=popped_node.val
            if(popped_level%2==0):
                arr[popped_level].append(popped_ele)
            else:
                arr[popped_level]=[popped_ele]+arr[popped_level]
            if(popped_node.left):
                queue.append((popped_node.left,popped_level+1))
            if(popped_node.right):
                queue.append((popped_node.right,popped_level+1))
        return arr.values()

