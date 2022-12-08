class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dic={}
        for x in arr:
            if(x in dic.keys() and dic[x]!=-1):
                dic[x]=-1
            elif(x not in dic.keys()):
                dic[x]=1
        l=[x[0] for x in filter(lambda x:x[1]!=-1,dic.items())]
        try:
            return l[k-1]
        except:
            return ""
