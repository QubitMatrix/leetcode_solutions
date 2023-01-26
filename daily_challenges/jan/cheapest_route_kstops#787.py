class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        tot_cost=[float("inf")]*n
        graph=defaultdict(list)
        for s,d,w in flights:
            graph[s].append((d,w))
        q=deque()
        q.append((src,0))
        while(q and k>-1):
            l=len(q)
            for x in range(l):#get all nodes at same level
                stop,cost=q.popleft()
                for new_stop,new_cost in graph[stop]:
                    if(cost+new_cost<tot_cost[new_stop]):
                        tot_cost[new_stop]=cost+new_cost
                        q.append((new_stop,tot_cost[new_stop]))
            k-=1
        return (tot_cost[dst] if tot_cost[dst]!=float("inf") else -1)
