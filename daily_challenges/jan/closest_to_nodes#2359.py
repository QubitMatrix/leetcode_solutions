class Solution:
    def bfs(self,node,edges,dis):
        queue=[]
        queue.append(node)
        dis[node]=0
        while(queue):
            ele=queue[0]
            queue=queue[1:]
            if(edges[ele]==-1):
                continue
            if(dis[edges[ele]]==-1):
                dis[edges[ele]]=dis[ele]+1
                queue.append(edges[ele])
            
        
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        dis1=[-1]*(len(edges))
        self.bfs(node1,edges,dis1)
        dis2=[-1]*(len(edges))
        self.bfs(node2,edges,dis2)
        minval=999999
        val=-1
        pos=-1
        for x in range(len(edges)):
            if(dis1[x]!=-1 and dis2[x]!=-1):
                val=max(dis1[x],dis2[x])
            if(val>=0 and val<minval):
                minval=val
                pos=x
        return pos
