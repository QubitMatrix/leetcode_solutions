# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getlevelorder(self,root,dic):
        stack=[]
        stack.append((root,0))
        while(len(stack)!=0):
            top=stack.pop()
            if(top[0]==None):
             if(top[1] in dic.keys()):
                dic[top[1]].append(-999)
             else:
                dic[top[1]]=[-999]
             continue
            else:
             if(top[1] in dic.keys()):
                dic[top[1]].append(top[0].val)
             else:
                dic[top[1]]=[top[0].val]
            stack.append((top[0].left,top[1]+1))
            stack.append((top[0].right,top[1]+1))

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        dic={}
        self.getlevelorder(root,dic)
        print(dic)
        for x in dic.values():
            y=list(reversed(x))
            if(x!=y):
                return False
        return True
