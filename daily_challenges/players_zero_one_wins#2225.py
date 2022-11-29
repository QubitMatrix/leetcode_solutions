class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic_los={}
        l3=[]
        for x in matches:
            if(x[0] not in dic_los.keys()):
                dic_los[x[0]]=0
            if(x[1] not in dic_los.keys()):
                dic_los[x[1]]=1
            else:
                dic_los[x[1]]+=1
        l1=[x for x in dic_los if dic_los[x]==0]
        l2=[x for x in dic_los if dic_los[x]==1]
        l1.sort()
        l2.sort()
        l3.append(l1)
        l3.append(l2)
        return(l3)
