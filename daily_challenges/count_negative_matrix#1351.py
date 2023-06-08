class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        count_r=0
        for x in range(len(grid)-1,-1,-1):
            count_r=0
            for y in range(len(grid[0])-1,-1,-1):
                if(grid[x][y]>=0):
                    break
                count_r+=1
            count+=count_r
            if(count_r==0):
                break
        return count
