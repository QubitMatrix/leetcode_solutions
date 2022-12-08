class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        dic={}
        s1_=s1.split()
        s2_=s2.split()
        for x in s1_:
            if(x in dic.keys() and dic[x]!=-1):
                dic[x]=-1
            elif(x not in dic.keys()):
                dic[x]=1
        d1=set([x[0] for x in filter(lambda x:x[1]!=-1,dic.items())])
        print(d1)
        dic={}
        for x in s2_:
            if(x in dic.keys() and dic[x]!=-1):
                dic[x]=-1
            elif(x not in dic.keys()):
                dic[x]=1
        d2=set([x[0] for x in filter(lambda x:x[1]!=-1,dic.items())])
        print(d2)
        
        return d1-set(s2_)|d2-set(s1_)
