class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1={}
        dic2={}
        for x in s:
            if(x in dic1.keys()):
                dic1[x]+=1
            else:
                dic1[x]=1
        for x in t:
            if( x in dic2.keys()):
                dic2[x]+=1
            else:
                dic2[x]=1
        if(dic1.keys()!=dic2.keys()):
            return False
        for x in dic1.keys():
            if(dic1[x]!=dic2[x]):
                return False
        return True
