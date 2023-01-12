class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree=defaultdict(list)
        for s,e in edges:
            tree[s].append(e)
            tree[e].append(s)
        ans=[0]*n

        def dfs(x,src):
            nonlocal ans
            count=Counter()
            for ele in tree[x]:
                if(ele!=src):
                    count+=dfs(ele,x)
            count[labels[x]]+=1
            ans[x]=count[labels[x]]
            return count
        dfs(0,-1)
        return ans
