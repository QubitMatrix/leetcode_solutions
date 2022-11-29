class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ss=""
        for x in range(0,len(s),2*k):
            s1=s[x:x+k]
            s1="".join(reversed(s1))
            s2=s[x+k:x+2*k]
            ss+=s1+s2
            print(ss)
        return ss
