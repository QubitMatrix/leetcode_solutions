class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dic={}
        for x in words1:
            if(x in dic.keys() and dic[x]!=-1):
                dic[x]=-1
            elif(x not in dic.keys()):
                dic[x]=1
        d1=set([x[0] for x in filter(lambda x:x[1]!=-1,dic.items())])
        dic={}
        for x in words2:
            if(x in dic.keys() and dic[x]!=-1):
                dic[x]=-1
            elif(x not in dic.keys()):
                dic[x]=1
        d2=set([x[0] for x in filter(lambda x:x[1]!=-1,dic.items())])
        return len(d1&d2)
