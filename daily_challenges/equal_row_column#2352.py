from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dic1=defaultdict(int)
        dic2=defaultdict(int)
        for x in range(len(grid)):
            s="-".join(map(str,grid[x]))
            dic1[s]+=1
        s=""
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                s+=str(grid[y][x])+"-"
            dic2[s[:-1]]+=1
            s=""
        count=0
        for x in dic1.keys():
            count+=dic1[x]*dic2[x]
        return(count)
