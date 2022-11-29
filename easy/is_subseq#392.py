class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s1=""
        for x in s:
            if(x in t):
                t=t[t.find(x)+1:]
                s1+=x
        return s1==s
