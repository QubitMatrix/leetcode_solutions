class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        o=s.count('0')
        ans=o
        for x in s:
            if(x=='0'):
                o-=1
            if(x=='1'):
                o+=1
            ans=min(ans,o)
        return ans
