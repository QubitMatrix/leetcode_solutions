# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=[]
        dic={}
        arr=[]
        queue.append((root,0))
        while(len(queue)!=0):
            front=queue[0]
            queue=queue[1:]
            if(front[0]!=None):
                print(front[0].val)
                if(front[1] in dic.keys()):
                    dic[front[1]].append(front[0].val)
                else:
                    dic[front[1]]=[front[0].val]
                queue.append((front[0].left,front[1]+1))
                queue.append((front[0].right,front[1]+1))
        for x in dic.values():
            arr.append(x)
        return arr
