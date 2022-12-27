class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if(set(ransomNote).intersection(set(magazine))!=set(ransomNote)):
            return False
        dic1={}
        dic2={}
        for x in ransomNote:
            if(x in dic1.keys()):
                dic1[x]+=1
            else:
                dic1[x]=1
        for x in magazine:
            if(x in dic2.keys()):
                dic2[x]+=1
            else:
                dic2[x]=1
        for x in dic1.keys():
            if(dic1[x]>dic2[x]):
                return False
        return True
