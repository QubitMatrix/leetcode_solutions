class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        swap=""
        s1=""
        count=0
        same=0
        dic={}
        for x in range(len(s)):
            if(s[x] in dic.keys()):
                dic[s[x]]+=1
                same=1
            else:
                dic[s[x]]=1
                
            if(swap=="" and s[x]!=goal[x]):
                swap=s[x]
                swap_pos=x
                count=1
                s1+=swap.upper()
            elif(swap!="" and s[x]!=goal[x] and count==1):
                s1=s1.replace(swap.upper(),s[x])
                s1+=swap
                count=2
            elif(s[x]!=goal[x] and count==2):
                return False
            else:
                s1+=s[x]
        if((s1.lower()==goal and count==2) or (same==1 and count==0)):
            return True
        else:
            return False
