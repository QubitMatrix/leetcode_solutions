class Solution:
    def dfs(self,grid,sr,sc,vis):
        count=1
        vis[sr][sc]=1
        if(sr-1>=0 and vis[sr-1][sc]==0 and grid[sr-1][sc]==1):
            count+=self.dfs(grid,sr-1,sc,vis)
        if(sc-1>=0 and vis[sr][sc-1]==0 and grid[sr][sc-1]==1):
            count+=self.dfs(grid,sr,sc-1,vis)
        if(sr+1<len(grid) and vis[sr+1][sc]==0 and grid[sr+1][sc]==1):
            count+=self.dfs(grid,sr+1,sc,vis)
        if(sc+1<len(grid[0]) and vis[sr][sc+1]==0 and grid[sr][sc+1]==1):
            count+=self.dfs(grid,sr,sc+1,vis)
        return count
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxcount=0
        vis=[]
        arr=[]
        t=[]
        for x in range(len(grid)):
            vis.append([])
            for y in range(len(grid[0])):
                t.append(0)
            vis[x]=t
            t=[]
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if(vis[x][y]==0 and grid[x][y]==1):
                    count=self.dfs(grid,x,y,vis)
                    if(count>maxcount):
                        maxcount=count
                        count=0
        return maxcount
