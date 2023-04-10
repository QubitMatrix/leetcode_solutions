class Solution:
    def matches(self,b,a):
        if(a=="(" and b==")" or a=="[" and b=="]" or a=="{" and b=="}"):
            return True
        else:
            return False
    def isValid(self, s: str) -> bool:
        stack=[]
        ope=["(","[","{"]
        for x in s:
            if (x in ope):
                stack.append(x)
            else:
                if(len(stack)==0):#extra closing bracket
                    return False
                if(self.matches(x,stack[-1])):
                    stack.pop()
                else:
                    return False# mismatch
        return len(stack)==0#extra opening bracket
                
