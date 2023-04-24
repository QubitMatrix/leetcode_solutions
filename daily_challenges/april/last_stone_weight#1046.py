import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #heapq implements min heap we need max, use negative values instead
        stones=[-1*x for x in stones]
        while(len(stones)>1):
            heapq.heapify(stones)
            x=heapq.heappop(stones)
            y=heapq.heappop(stones)
            if(x!=y):
                heapq.heappush(stones,-1*int(math.fabs(x-y)))
        return -1*stones[0] if len(stones)==1 else 0
