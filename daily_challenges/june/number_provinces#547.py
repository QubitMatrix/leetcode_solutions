from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        for z in range(n):
            for x in range(n):
                for y in range(n):
                    isConnected[x][y]=isConnected[x][y] or (isConnected[x][z] and isConnected[z][y])
        count=1
        dis_set=defaultdict(int)
        for x in range(n):
            if(dis_set[x]==0):
                dis_set[x]=count
                count+=1
            province=dis_set[x]
            for y in range(n):
                if(isConnected[x][y]):
                    dis_set[y]=province
        return(count-1)
        
