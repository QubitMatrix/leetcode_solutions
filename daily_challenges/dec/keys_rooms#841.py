class Solution:
    def dfs(self,vis,dic,src):
        for x in dic[src]:
            if(vis[x]==0):
                vis[x]=1
                self.dfs(vis,dic,x)
        
        
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        dic={}
        for x in range(len(rooms)):
            dic[x]=rooms[x]
        vis=defaultdict(lambda:0)
        arr=[y for x in rooms for y in x]
        src=0    
        vis[0]=1
        self.dfs(vis,dic,src)
        if(len(vis)!=len(rooms)):
            return False
        else:
            return True
