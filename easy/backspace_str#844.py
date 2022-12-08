class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i=0
        while(i<len(s)):
            if(s[i]=="#"):
                if(i==0):
                    s=s[i+1:]
                else:
                    s=s[:i-1]+s[i+1:]
                i=i-2
            i+=1
            if(i<0):
                i=0
        i=0
        while(i<len(t)):
            if(t[i]=="#"):
                if(i==0):
                    t=t[i+1:]
                else:
                    t=t[:i-1]+t[i+1:]
                i=i-2
            i+=1
            if(i<0):
                i=0
        return s==t
