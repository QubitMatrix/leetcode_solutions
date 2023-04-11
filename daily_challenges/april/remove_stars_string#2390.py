class Solution:
    def removeStars(self, s: str) -> str:
        pos=0
        pos1=0
        s1=list(s)
        while(pos<len(s)):
            if(s[pos]=='*'):
                pos1=pos1-2
            else:
                s1[pos1]=s[pos]
            pos+=1
            pos1+=1
        s1="".join(s1[:pos1])
        return(s1)
