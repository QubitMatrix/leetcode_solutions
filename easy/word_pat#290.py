from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic=defaultdict(str)
        s1=""
        l=s.split()
        if(len(l)!=len(pattern)):
            return False
            
        for x in range(len(l)):
            if(dic[l[x]]==''):
                if(pattern[x] in dic.values()):
                    return False
                else:
                    dic[l[x]]=pattern[x]
            else:
                if(dic[l[x]]!=pattern[x]):
                    return False
            
        return True
