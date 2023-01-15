class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        union1={}
        tree=defaultdict(list)
        node_val=defaultdict(set)
        for s,e in edges:
            tree[s].append(e)
            tree[e].append(s)
            node_val[vals[s]].add(s)
            node_val[vals[e]].add(e)
        ans=len(vals)
        def find(x):
            union1.setdefault(x,x)
            if x!=union1[x]:
                union1[x]=find(union1[x])
            return union1[x]
        def union(x,y):
            union1[find(x)]=find(y)
        for v in sorted(node_val.keys()):
            for node in node_val[v]:
                for z in tree[node]:
                    if(vals[z]<=v):
                        union(node,z)
            count=defaultdict(int)
            for node in node_val[v]:
                count[find(node)]+=1
            for root in count.keys():
                ans+=comb(count[root],2)
        return ans
