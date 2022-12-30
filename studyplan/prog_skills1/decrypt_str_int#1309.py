class Solution:
    def freqAlphabets(self, s: str) -> str:
        s1=""
        dic={}
        for x in range(1,27):
            dic[x]=chr(ord('a')+x-1)
        x=0
        while(x<len(s)):
            if(x+2<len(s) and s[x+2]=="#"):
                s1+=dic[int(s[x:x+2])]
                x+=3
                
            else:
                s1+=dic[int(s[x])]
                x+=1
        return s1
