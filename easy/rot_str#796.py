class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        l=[]
        while(1):
            try:
                a=s.index(goal[0],1)
                s=s[a:]+s[:a]
                if(s==goal):
                    return True
                if(s in l):
                    break
                l.append(s)
            except:
                return s==goal
