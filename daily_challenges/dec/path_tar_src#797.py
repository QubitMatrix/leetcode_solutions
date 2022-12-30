import copy
class Solution:
    def DFS(self,edges,src,des,arr,path):
        arr.append(src)
        for x in edges[src]:
            self.DFS(edges,x,des,arr,path)
        if(src==des):
            path.append(copy.deepcopy(arr))     
        arr.pop()
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        edges={}
        arr=[]
        path=[]
        for x in range(len(graph)):
            if(x not in edges.keys()):
                edges[x]=graph[x]
        self.DFS(edges,0,len(graph)-1,arr,path)
        return(path)
