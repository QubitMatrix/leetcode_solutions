class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dic={}
        for x in s:
            if(x in dic.keys()):
                dic[x]+=1
            else:
                dic[x]=1
        return(len(set(dic.values()))==1)
