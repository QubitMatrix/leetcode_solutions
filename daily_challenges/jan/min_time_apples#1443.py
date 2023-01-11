class Solution:
    def dfs(self,src,par,tree,hasApple):
        res=0
        for x in tree[src]:
            if(x!=par):
                res+=self.dfs(x,src,tree,hasApple)
                
        if res or hasApple[src]:
            return res+2
        return res
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree=defaultdict(list)
        for s,e in edges:
            tree[s].append(e)
            tree[e].append(s)
        return max(self.dfs(0,-1,tree,hasApple)-2,0)
