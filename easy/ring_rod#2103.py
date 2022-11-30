class Solution:
    def countPoints(self, rings: str) -> int:
        dic={}
        for x in range(0,len(rings),2):
            if(rings[x+1] in dic.keys()):
                dic[rings[x+1]].add(rings[x])
            else:
                dic[rings[x+1]]=set(rings[x])
        return(list(dic.values()).count({'R','G','B'}))
