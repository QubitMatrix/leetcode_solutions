class Solution:
    def dfs(self,mat,visited,src,edges):
        visited[src]=1
        count=0
        for x in range(len(mat)):
            if(mat[src][x]):
                if(not visited[x]):
                    count+=self.dfs(mat,visited,x,edges)
                edges[0]+=1
        return count+1


    def DFS(self,mat):
        visited=[0 for x in range(len(mat))]
        comp=0
        count=0
        ans=0
        edges=[0]
        for x in range(len(mat)):
            if(not visited[x]):
                count+=self.dfs(mat,visited,x,edges)
                edge=edges[0]//2
                if(edge==(count*(count-1)//2)):
                    ans+=1
                edges=[0]
                count=0
                comp+=1
        return(ans)
            


    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        t=[]
        mat=[]
        t=[]
        for x in range(n):
            for y in range(n):
                t.append(0)
            mat.append(t)
            t=[]
        for x,y in edges:
            mat[x][y]=1
            mat[y][x]=1
        ans=self.DFS(mat)
        return ans
