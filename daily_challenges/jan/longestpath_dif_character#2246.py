class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree=defaultdict(list)
        for e,st in enumerate(parent):
            tree[st].append(e)
        ans=1
        def dfs(src):
            nonlocal ans
            m1=m2=0
            for x in tree[src]:
                t=dfs(x)
                if(s[x]!=s[src]):
                    if(t>m1):
                        m2=m1
                        m1=t
                    elif(t>m2):
                        m2=t
            ans=max(ans,m1+m2+1)
            return m1+1
        dfs(0)
        return ans
