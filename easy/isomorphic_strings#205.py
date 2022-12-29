class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic={}
        for x in range(len(s)):
            if(s[x] in dic.keys()):
                if(dic[s[x]]!=t[x]):
                    return False
            else:
                if(t[x] not in dic.values()):
                    dic[s[x]]=t[x]
                else:
                    return False
        return True
