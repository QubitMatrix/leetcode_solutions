class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=sorted(s)
        t=sorted(t)
        for x in range(len(s)):
            if(s[x]!=t[x]):
                return t[x]
        return t[-1]
