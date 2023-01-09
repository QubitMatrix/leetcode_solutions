class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten=[]
        fresh=0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if(grid[x][y]==1):
                    fresh+=1
                elif(grid[x][y]==2):
                    rotten.append((x,y))
        mins=0
        while rotten and fresh!=0:
            mins+=1
            for z in range(len(rotten)):
                x,y=rotten[0]
                rotten=rotten[1:]
                if(x+1<len(grid) and grid[x+1][y]==1):
                    grid[x+1][y]=2
                    fresh-=1
                    rotten.append((x+1,y))
                if(x>0 and grid[x-1][y]==1):
                    grid[x-1][y]=2
                    fresh-=1
                    rotten.append((x-1,y))
                if(y+1<len(grid[0]) and grid[x][y+1]==1):
                    grid[x][y+1]=2
                    fresh-=1
                    rotten.append((x,y+1))
                if(y>0 and grid[x][y-1]==1):
                    grid[x][y-1]=2
                    fresh-=1
                    rotten.append((x,y-1))
        return mins if fresh==0 else -1
