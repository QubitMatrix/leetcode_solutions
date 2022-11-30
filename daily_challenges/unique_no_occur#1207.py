class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic={}
        for x in arr:
            if(x in dic.keys()):
                dic[x]+=1
            else:
                dic[x]=1
        count=set(dic.values())
        return len(count)==len(dic.values())
