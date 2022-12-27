class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic={}
        for x in range(len(s)):
            if(s[x] in dic.keys()):
                dic[s[x]][1]+=1
            else:
                dic[s[x]]=list((x,1))
        dic=[x for x in dic.items() if x[1][1]==1]
        dic=sorted(dic,key=lambda x:x[1][0])
        try:
            return(dic[0][1][0])
        except:
            return -1
