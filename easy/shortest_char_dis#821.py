class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans=[]
        minpos=s.index(c)
        for x in range(len(s)):
            dif=minpos-x
            if(s[x]==c):
                if (minpos<x):
                    minpos=x
            if(dif<0):
                try:
                    dif2=s.index(c,x)-x
                    ans.append(int(min(math.fabs(dif),dif2)))
                except:
                    ans.append(-1*dif)
            else:
                ans.append(dif)
        return ans
